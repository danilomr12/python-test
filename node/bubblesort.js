
    
function sort(arr) {
    let n = arr.length
    console.log(n)
    for(let i = n-1; i>=1; i--){
        console.log("first loop " +i)
        for(let j = 0; j <= i -1; j++){
            console.log("j: " + j)
            console.log("i: " + i)
            console.log(arr)
            if(arr[j] > arr[j+1]){
                console.log("swap")
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            }
            
        }
    }    
    console.log("end sort " +arr)
}

// let a = [1,2,3,4,5]
// console.log(a)

// [a[2], a[3]] = [a[3], a[2]]
// console.log(a)
 sort([8,5,88,1,200,6,4,3,1])