const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
    if (error.message.includes("Reason: Already Verified")) {
      console.log("Contract is already verified.");
    } else {
      console.error("Verification error:", error);
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
    if (error.message.includes("Reason: Already Verified")) {
      console.log("Contract is already verified.");
    } else {
      console.error("Verification error:", error);
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
    if (error.message.includes("Reason: Already Verified")) {
      console.log("Contract is already verified.");
    } else {
      console.error("Verification error:", error);
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
    if (error.message.includes("Reason: Already Verified")) {
      console.log("Contract is already verified.");
    } else {
      console.error("Verification error:", error);
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
    if (error.message.includes("Reason: Already Verified")) {
      console.log("Contract is already verified.");
    } else {
      console.error("Verification error:", error);
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
    if (error.message.includes("Reason: Already Verified")) {
      console.log("Contract is already verified.");
    } else {
      console.error("Verification error:", error);
    }
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
const hre = require("hardhat");

async function main() {
  const Lock = await hre.ethers.getContractFactory("Lock");
  const lock = await Lock.deploy(1693948800);

  await lock.deployed();

  console.log("Lock deployed to:", lock.address);

  // Verify the contract on Etherscan
  try {
    await hre.run("verify:verify", {
      address: lock.address,
      constructorArguments: [1693948800],
    });
    console.log("Contract verified on Etherscan!");
  } catch (error) {
    console.error("Verification failed:", error);
  }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
