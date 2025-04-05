// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

// A contract is a collection of functions and data (its state). Once deployed, a contract resides at a specific address on the Ethereum blockchain.
contract Lock {

    uint public unlockTime;
    address payable public owner;

    // Events allow lightweigth clients to react on-chain events
    event Withdrawal(uint amount, uint time);

    // Constructor
    constructor(uint _unlockTime) payable {
        require(_unlockTime > block.timestamp, "Unlock time should be in the future");

        unlockTime = _unlockTime;
        owner = payable(msg.sender);
    }

    function withdraw() public {
        // require helps to not waste gas in case of a failed transaction
        require(block.timestamp >= unlockTime, "You can't withdraw yet");
        require(msg.sender == owner, "You aren't the owner");

        emit Withdrawal(address(this).balance, block.timestamp);

        owner.transfer(address(this).balance);
    }
}
