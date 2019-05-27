
var web3;

window.onload = function() {
    // add token making an account infura.io
    const token = ''; 
    web3 = new Web3(`https://ropsten.infura.io/v3/${token}`);
    console.log('version', web3.version);

    getERC20TokenBalance(tokenAddress, walletAddress, (balance) => {
        console.log(balance);
        document.getElementById('result').innerText = balance;
    })
    drawMerchants();
}


let tokenAddress = '0x2A65D41dbC6E8925bD9253abfAdaFab98eA53E34';
let walletAddress = '0x821e28109872cad442da8d8335be37d317d4f1e7';

async function getERC20TokenBalance(tokenAddress, walletAddress, callback) {
    let abi = [
        {"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"},
        {"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"type":"function"}
    ];
    console.log('web3', web3);

    callback(await web3.eth.getBalance(tokenAddress));
    
    /* let contract = new web3js.eth.Contract(minABI, tokenAddress);
    console.log(contract);
    contract.methods.balanceOf(walletAddress).call(
        (error, balance) => {
            console.log(balance);
            contract.methods.decimals().call(
                (error, decimals) => {
                    console.log(balance);
                    console.log(decimals);
                    balance = balance / (10**decimals);
                    callback(balance);
                });
    }); */
}

function drawMerchants() {
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    xhr.open("GET", "http://10.16.181.1:8000/api/ongs/?format=json", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            // WARNING! Might be evaluating an evil script!
            var json = xhr.response;
            for (var i = 0; i < json.length; i++){

                var obj = json[i];
                for (var key in obj){
                    var value = obj[key];
                    var innerText = key + ": " + value ;
                    var el = document.createElement('div');
                    el.innerText = innerText;
                    document.getElementById('ong_result').appendChild(el);


                }
            }

        }
    }
    xhr.send();
}
