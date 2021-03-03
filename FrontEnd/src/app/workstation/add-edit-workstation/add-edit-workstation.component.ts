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
    this.WorkstationId = this.workstation.WorkstationId;
    this.Xposition = this.workstation.Xposition;
    this.Yposition = this.workstation.Yposition;
    this.Status = this.workstation.Status;
  }

  // tslint:disable-next-line:typedef
  addWorkstation(){
    const val = {WorkstationId: this.WorkstationId,
      Xposition: this.Xposition,
      Yposition: this.Yposition,
      Status: this.Status};
    this.service.addWorkstation(val).subscribe(res => {
      alert(res.toString());
    });
  }
}
