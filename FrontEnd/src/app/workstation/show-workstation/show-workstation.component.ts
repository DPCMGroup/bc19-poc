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

  editClick(item: any){
    this.workstation = item;
    this.ModalTitle = 'Edit Workstation';
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
  deleteClick(item: { WorkstationID: any; }){
    if (confirm('Are you sure??')){
      this.service.deleteWorkstation(item.WorkstationID).subscribe(data => {
        alert(data.toString());
        this.refreshWorkstationList();
      });
    }
  }
}
