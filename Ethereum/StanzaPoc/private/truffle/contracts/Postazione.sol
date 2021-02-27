pragma solidity ^0.5.16;

contract Stanza {
    struct Postazione {
        
        uint256 x;   
        uint256 y;
        uint256 id;    //id tag NFC
    }


    // Array di postazioni
    Postazione[] postazioni;
 
    //Numero Postazioni non eliminate
    uint256 public nrPostazioni = 0;
    
     // Aggiungi una postazione nell'array delle postazioni.
    function addPostazione( uint256 x, uint256 y, uint256 id) public {
        
        Postazione memory postazione = Postazione(
            x,
            y,
            id
        );
        postazioni.push(postazione);

        nrPostazioni++;
    }

        
    //Settaggio a 0 dei campi della postazione da eliminare
    //input: indice dell'array delle postazioni
    function deletePostazione(uint256 index) public {
        Postazione storage postazione = postazioni[index];
        postazione.x=0;
        postazione.y=0;
        postazione.id=0;
        
        nrPostazioni--;
    }

     // Get postazione dato l'indice dell'array di postazioni
    function getPostazione(uint256 index) view public returns(uint256, uint256, uint256) {
        Postazione storage postazione = postazioni[index];
        return (postazione.x, postazione.y, postazione.id);
    }
}
    