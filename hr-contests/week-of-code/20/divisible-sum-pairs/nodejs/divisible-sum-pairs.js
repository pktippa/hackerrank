process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data',readInput).on('end', processData);

function readInput(data) {
    input_stdin += data;
}

function processData() {
    input_stdin_array = input_stdin.split("\n");
    main();    
}

function readLine() {
    return input_stdin_array[input_currentline++];
}

function main(){
	var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var k = parseInt(n_temp[1]);
    a = readLine().split(' ');
    a = a.map(Number);
    var count = 0;
    for(var i=0;i<a.length-1;i++){
    	for(j=i+1;j<a.length;j++){
    		if((a[i]+a[j]) % k === 0){
    			count+=1;
    		}
    	}
    }
    console.log(count);
}