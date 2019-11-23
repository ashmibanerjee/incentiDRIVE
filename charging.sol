pragma solidity ^0.5.13;

contract ChargingContract {
    
    address owner;
    bool unitTransfered;
    uint unitPrice;
    
    address[] wallets;
    
    constructor() public payable {
        owner = msg.sender; //Change
        unitTransfered = false;
        unitPrice = 10; //random value
    }
    
    modifier oneOwner {
        require (msg.sender == owner);
        _;
    }
    
    modifier isTransfered {
        require (unitTransfered == true);
        _;
    }
    
    function setup(address _charger) public oneOwner {
        wallet = _charger;
    }
    
    function pay() private isTransfered {
        wallet.transfer(unitPrice);
        unitTransfered = false;
    }
    
    function unitCharged() public oneOwner {
        unitTransfered = true;
        pay();
    }
    
    
}
