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
  ModalTitle: string | undefined;
  workstation: any;
  ActivateAddEditWorkstationComp = false;
  ngOnInit(): void {
    this.refreshWorkstationList();
  }

  addClick(){
    this.workstation = {WorkstationID : 0, WorkstationName : ''};
    this.ModalTitle = 'Add workstation';
    this.ActivateAddEditWorkstationComp = true;
  }

  closeClick(){
    this.ActivateAddEditWorkstationComp = false;
    this.refreshWorkstationList();
  }
  refreshWorkstationList(){
    this.service.getWorkstationList().subscribe(data => {
      this.WorkstationList = data;
    });
  }
}
