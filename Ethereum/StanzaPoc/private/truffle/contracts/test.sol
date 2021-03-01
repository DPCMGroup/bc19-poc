// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.7.4;

contract SimpleStorage {
    
 struct Postazione {
     uint x;
     uint y;
     string stato;
 }

 event creataPostazione(string id, uint x, uint y, string stato);
 event eliminataPostazione(string id, uint x, uint y, string stato);
 
 //dati della stanza
 uint dim1;
 uint dim2;
 mapping (string => Postazione) public postazioni; 
 
// marcare mapping PUBLIC => getter implicito
// se id non presente nel mapping, getter restituisce: (0,0,"")
 
 function setDimensioniStanza(uint _dim1, uint _dim2) public {
     dim1=_dim1;
     dim2=_dim2;
 }
 
 function creaPostazione (string memory _id, uint _x, uint _y, string memory _stato) public {
     postazioni[_id]=Postazione(_x, _y, _stato);
     emit creataPostazione(_id, postazioni[_id].x, postazioni[_id].y, postazioni[_id].stato);
 }
 
 function eliminaPostazione (string memory _id) public {
     delete postazioni[_id];
     emit eliminataPostazione(_id, postazioni[_id].x, postazioni[_id].y, postazioni[_id].stato);
 }
    
}
    