
let arr1 = [5,6,7]
let arr2 = [true,false,'hello']
let newArr = arr1.concat(arr2)
console.log(newArr)
newArr.push('loop', 'bigguy')
console.log(newArr)
newArr.unshift('start', 10)
console.log(newArr)
newArr.pop()
newArr.pop()
newArr.shift()
console.log(newArr)
console.log(newArr.slice(2,5))
console.log(newArr.includes(4))
