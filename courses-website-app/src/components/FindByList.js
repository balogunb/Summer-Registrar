import React, {Component} from 'react'
import Grid from '@material-ui/core/Grid'
import TextField from '@material-ui/core/TextField'
import FindBy from '../components/FindBy'





class FindByList extends Component{
  state = {
    searchString:''

  }

  constructor(){
    super()
    this.getFindBy()

  }

  getFindBy = () =>{
    return ['Course Title', 'School Name','Location']
  }
}
