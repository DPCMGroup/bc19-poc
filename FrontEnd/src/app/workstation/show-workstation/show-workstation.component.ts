import { Component, OnInit } from '@angular/core';
import {SharedService} from '../../shared.service';

@Component({
  selector: 'app-show-workstation',
  templateUrl: './show-workstation.component.html',
  styleUrls: ['./show-workstation.component.css']
})
export class ShowWorkstationComponent implements OnInit {

  constructor(private service: SharedService) { }

  WorkstationList: any = [];
  ngOnInit(): void {
    this.refreshWorkstationList();
  }

  refreshWorkstationList(){
    this.service.getWorkstationList().subscribe(data => {
      this.WorkstationList = data;
    });
  }
}
