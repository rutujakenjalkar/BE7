// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

contract Bank{

    address public owner;
    
    constructor(){
        owner=msg.sender;
    }

    function deposit() public payable{
        require(msg.value>0,"You need to spend money");
    } 
     function withdraw(uint amount) public {
        require(msg.sender==owner,"You are not the owner");
        payable(msg.sender).transfer(amount);
    }

    function getBalance() public view returns(uint){
        return address(this).balance;
    }

}
