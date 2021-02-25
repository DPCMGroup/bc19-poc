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

  // tslint:disable-next-line:typedef
  addClick(){
    this.workstation = {WorkstationID : 0, WorkstationX : '', WorkstationY : ''};
    this.ModalTitle = 'Add workstation';
    this.ActivateAddEditWorkstationComp = true;
  }

  // tslint:disable-next-line:typedef
  closeClick(){
    this.ActivateAddEditWorkstationComp = false;
    this.refreshWorkstationList();
  }
  // tslint:disable-next-line:typedef
  refreshWorkstationList(){
    this.service.getWorkstationList().subscribe(data => {
      this.WorkstationList = data;
    });
  }
}
