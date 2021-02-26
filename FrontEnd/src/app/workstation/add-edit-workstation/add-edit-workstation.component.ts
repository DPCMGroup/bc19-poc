import {Component, Input, OnInit} from '@angular/core';
import { SharedService } from '../../shared.service';

@Component({
  selector: 'app-add-edit-workstation',
  templateUrl: './add-edit-workstation.component.html',
  styleUrls: ['./add-edit-workstation.component.css']
})
export class AddEditWorkstationComponent implements OnInit {
  constructor(private service: SharedService ) { }

  @Input() workstation: any;
  WorkstationID: string | undefined;
  WorkstationX: number | undefined;
  WorkstationY: number | undefined;

  ngOnInit(): void {
    this.WorkstationID = this.workstation.WorkstationID;
    this.WorkstationX = this.workstation.WorkstationX;
    this.WorkstationY = this.workstation.WorkstationY;
  }

  addWorkstation(){
    const val = {WorkstationID: this.WorkstationID,
      WorkstationX: this.WorkstationX,
      WorkstationY: this.WorkstationY};
    this.service.addWorkstation(val).subscribe(res => {
      alert(res.toString());
    });
  }

  updateWorkstation(){
    const val = {WorkstationID: this.WorkstationID,
      WorkstationX: this.WorkstationX,
      WorkstationY: this.WorkstationY};
    this.service.updateWorkstation(val).subscribe(res => {
      alert(res.toString());
    });
  }

}
