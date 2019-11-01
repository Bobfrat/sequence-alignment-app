import React, { Component } from 'react'
import BootstrapTable from 'react-bootstrap-table-next'
import ToolkitProvider, { Search } from 'react-bootstrap-table2-toolkit';

export default class ResultsTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null,

    };
  }

  render() {
    const { SearchBar } = Search;
    const tableColumns = [
      {
        dataField: 'dna',
        text: 'Sequence',
        sort: true
      }, 
      {
        dataField: 'protein',
        text: 'Protein',
        sort: true
      }, 
      {
        dataField: 'start_position',
        text: 'Start Position',
        sort: true
      }, 
      {
        dataField: 'end_position',
        text: 'End Position',
        sort: true
      }
    ];

    let tableData = [];
    let rowObj = {};
    this.props.data.map((item, idx) => {
      rowObj = {
        dna: item.dna,
        protein: item.protein || 'No Match',
        start_position: item.start_position || 'No Match',
        end_position: item.end_position || 'No Match'
      }
      tableData.push(rowObj)
    });

    if (tableData.length === 0) {
      return null;
    }
    return (
      <div className="container" style={{ marginTop: 50 }}>
        <ToolkitProvider
          striped
          hover
          keyField="dna"
          data={ tableData }
          columns={ tableColumns }
          search
        >
          {
            props => (
              <div>
                <h3>Filter previous results:</h3>
                <SearchBar { ...props.searchProps } />
                <hr />
                <BootstrapTable
                  { ...props.baseProps }
                />
              </div>
            )
          }
        </ToolkitProvider>
      </div>
    );
  }
}