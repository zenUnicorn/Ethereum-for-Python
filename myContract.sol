pragma solidity ^0.5.13;

//With public in the code you can call the code in the deploy, else it won't show in the deploy area.
contract WorkingWithVariable {
    //unsigned integer
    uint256 public myUint;

    function setMyUint(uint _myUint) public {
        myUint = _myUint;
    }

    //Booleans
    bool public myBool;

    function setMyBool(bool _myBool) public {
        myBool = _myBool;
    }
    //Variables: Interger Wrap around - uint8 (0-255), uint8 (0-255) while int8 (-128 to 127)
    uint8 public myUint8;

    //Increment and Decrement
    function IncrementUint() public {
        myUint8++;
    }

    function DecrementUint() public {
        myUint8--; 
    }

    //Variables: Addresses
    address public myAddress;
    function setMyAddress (address _address) public {
        myAddress = _address;
    }

    //let's get the balance of an address..returns value in wei
    function getBalance () public view returns(uint) {
        return myAddress.balance;
    }

    //Variables: Strings - Always add the memory in the string so that the comouter knows where to store the datatype
    string public myString;
    function setString(string memory _myString) public {
        myString = _myString;
    }
    


}