import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

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
  // tslint:disable-next-line
  ActivateAddEditWorkstationComp: boolean = false;
  ngOnInit(): void {
    this.refreshWorkstationList();
  }

  // tslint:disable-next-line:typedef
  addClick(){
    this.workstation = {
      WorkstationId: 0,
      Xposition: '',
      Yposition: '',
      Status: 'NonDisponibile'};
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

  // tslint:disable-next-line:typedef
  deleteClick(item: { WorkstationId: any; }){
    if (confirm('Are you sure??')){
      this.service.deleteWorkstation(item.WorkstationId).subscribe(data => {
        alert(data.toString());
        this.refreshWorkstationList();
      });
    }
  }
}
