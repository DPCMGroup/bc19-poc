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
  WorkstationId: number | undefined;
  Xposition: number | undefined;
  Yposition: number | undefined;
  Status: string | undefined;

  ngOnInit(): void {
    this.WorkstationId = this.workstation.WorkstationID;
    this.Xposition = this.workstation.WorkstationX;
    this.Yposition = this.workstation.WorkstationY;
    this.Status = this.workstation.Status;
  }

  // tslint:disable-next-line:typedef
  addWorkstation(){
    const val = {WorkstationID: this.WorkstationId,
      WorkstationX: this.Xposition,
      WorkstationY: this.Yposition,
      Status: this.Status};
    this.service.addWorkstation(val).subscribe(res => {
      alert(res.toString());
    });
  }

  // tslint:disable-next-line:typedef
  updateWorkstation(){
    const val = {WorkstationID: this.WorkstationId,
      WorkstationX: this.Xposition,
      WorkstationY: this.Yposition,
      Status: this.Status};
    this.service.updateWorkstation(val).subscribe(res => {
      alert(res.toString());
    });
  }

}
