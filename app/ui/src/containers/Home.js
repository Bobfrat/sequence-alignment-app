import React, { Component } from 'react';
import Alert from 'react-bootstrap/Alert'
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import ResultsTable from '../components/ResultsTable';
import LoaderButton from '../components/LoaderButton';
import './Home.css';


export default class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: false,
      data: JSON.parse(localStorage.getItem('searchResults')) || [],
      dna: ''
    };

    // const url = 'wss://gdjcxvsub6.execute-api.us-east-2.amazonaws.com/testing';
    // const connection = new WebSocket(url);

    // connection.onerror = e => {
    //   console.error('WebSocket Connection Error');
    //   return (
    //     <div>
    //       <Alert variant="danger">
    //         <Alert.Heading>Error!</Alert.Heading>
    //         <p>
    //           Error connecting to WebSocket
    //         </p>
    //       </Alert>
    //     </div>
    //   )
    // }

    // connection.onopen = e => {
    //   console.log('Connected to WebSocket')
    //   // const message = JSON.stringify({action: 'history'});
    //   // connection.send(message);
    // }
  }
  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };

  handleSubmit = async event => {
    event.preventDefault();
    // this.setState({ isLoading: true });  // 
    const settings = {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        dna_sequence: this.state.dna
      })
    };
    try {
      const response = await fetch(process.env.REACT_APP_API_ENDPOINT, settings);
      if (!response.ok) {
        throw Error(response.statusText);
      }
      this.setState({ isLoading: false });

      const data = await response.json();
      let updatedData = data.concat(this.state.data)
      localStorage.setItem('searchResults', JSON.stringify(updatedData))
      this.setState({ data: updatedData });

    } catch (e) {
      alert(e.message);
      this.setState({ isLoading: false });
    }
  };

  render() {
    return (
      <div className='Home'>
        <div className='container'>
          <h1>Search for a DNA sequence:</h1>
          <Row style={{paddingTop: '20px'}}>
            <Col sm={3}/>
            <Col sm={6}>
              <Form onSubmit={this.handleSubmit}>
                <Form.Group controlId="dna">
                  <Form.Label>DNA Sequence:</Form.Label>
                  <Form.Control as='textarea' rows='2' value={this.state.dna} onChange={this.handleChange} />
                </Form.Group>
                <LoaderButton
                  block
                  bsSize="large"
                  type="submit"
                  isLoading={this.state.isLoading}
                  text="Search"
                  loadingText="Searching…"
                />
              </Form>
            </Col>
            <Col sm={3}/>
          </Row>
          {this.state.data.length > 0 && (
            <Row>
              <ResultsTable data={this.state.data} />
            </Row>
          )}
        </div>
      </div>
    );
  }
}
