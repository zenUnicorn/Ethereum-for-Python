// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.5.13;

contract SendMoneyExample {

    uint public balanceRecieved;

    //keyword in order for it to be able to receive money
    function recieveMoney() public payable{
        //gets the balance of the smart contract
        balanceRecieved += msg.value;
    }
    //lets get the balance of the smart contract address
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }
    //withdraw funds to a the sender's wallet
    function withdrawMoney() public {
        address payable to = msg.sender;
        to.transfer(this.getBalance());
    }     
    //function to tell the smart contract where to transfer the money to
    function withdrawMoneyTo(address payable _to) public {
        _to.transfer(this.getBalance()); 
    }
    
} 
