pragma solidity ^0.5.16;

contract SimpleStorage {
 struct Position {
        uint x;
        uint y;
    }
    uint x;
    uint y;

    uint [] postazioni;

    
    mapping (uint => Position) positions;
    uint[] public positionId;

function creaStanza(uint _x,uint _y)public{
  x=_x;
  y=_y;
}

  function setPosition(uint _uint, uint _x, uint _y) public {
        var position = positions[_uint];
        //SimpleStorage.Position= positions[_uint];
        position.x = _x;
        position.y = _y;
        
        positionId.push(_uint) -1;

    }
    function getPositions() view public returns (uint[]) {
        return positionId;
    }
    function getPosition(uint _uint) view public returns (uint, uint) {
        return (positions[_uint].x, positions[_uint].y);
    }
    function deletePosition(uint _uint) public {
        positionId.pop(_uint);
    }
}


