//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;

contract StudentData{

    struct Student{
        uint Rollno;
        string Name;
        uint Marks;

    }

    Student[] public Students;

    address public owner;
    constructor(){
        owner=msg.sender;

    }

    //ADD student to the student list
    function addStudent(uint _rollno,string memory _name,uint _marks) public{
        Students.push(Student(_rollno,_name,_marks));   
    }

    function getStudent(uint index) public view returns (uint,string memory,uint){
        require(index<Students.length,"student does not exist");
        Student memory s =Students[index];
        return (s.Rollno,s.Name,s.Marks);
    }

    //function to get total number of students
    function getotalStudents() public view returns(uint){
        return Students.length;
    }


    fallback() external payable{}
    receive() external payable { }
    
    function getBalance() public view returns(uint){
        return address(this).balance;
    }

}
