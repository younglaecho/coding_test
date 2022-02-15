const Box = document.querySelector('.visualization_box')
const makeButton = document.querySelector('.makeButton')
const startButton = document.querySelector('.startButton')
const length = document.querySelector('#length')
const matrixStr = document.querySelector('#matrix')
const result = document.querySelector('.result')
let matrix = []
let visited = []
// const name = document.getElementById('#length').value

const dx = [1, -1, 0, 0]
const dy = [0, 0, 1, -1]
let number = 0


makeButton.addEventListener('click', () => {
  // 다시 입력했을때 리렌더링하기
  if(Box.hasChildNodes()){
    matrix = []
    visited = []
    while(Box.hasChildNodes()) {
      Box.removeChild(Box.firstChild)
    }
  }

  // matrix 만들기
  let matrix1 = matrixStr.value.split("\n")
  for (element of matrix1) {
    matrix.push(element.split(""))
  }
  
  // visited 만들기
  for (let i=0;i<length.value;i++) {
    let list = []
    for (let j=0;j<length.value;j++){
      list.push(0)
    }
    visited.push(list)
  }

  // 흰검 칠하기
  smallLength = 500/length.value
  let x = 0
  let y = 0
  for (list of matrix) {
    for (element of list) {
      let smallBox = document.createElement('div')
      smallBox.style.width= smallLength +'px'
      smallBox.style.height= smallLength +'px'
      if (element == '0') {
        smallBox.className= `smallBox blackSmallbox x${x}y${y}` 
      } else {
        smallBox.className= `smallBox whiteSmallbox x${x}y${y}`
      }
      Box.appendChild(smallBox)
      x++
      if(x==length.value) {
        x = 0
        y++
      }
    }
  }
})

const BFS = (y0, x0) => {    
  const queue = [[y0,x0]]

  // 랜덤 생상 주기
  const color = '#' + Math.round(Math.random() * 0xffffff).toString(16)
  let selectedBox = document.querySelector(`.x${x0}y${y0}`)
  selectedBox.style.backgroundColor = `${color}`
  
  while (queue) {
    let position =queue.shift()
    if(!position){
      break
    }
    console.log(position)
    console.log(visited)
    let x = position[1]
    let y = position[0]
    visited[y][x] = number
    for(let i=0;i<4;i++) {
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx && nx < length.value && 0 <= ny && ny < length.value) {
        if (visited[ny][nx]==0 && matrix[ny][nx]=='1') {
          selectedBox = document.querySelector(`.x${nx}y${ny}`)
          selectedBox.style.backgroundColor = `${color}`
          visited[ny][nx] = number
          queue.push([ny,nx])  
        }
      } 
    }
  }
}



startButton.addEventListener('click', ()=> {
  for (let i=0;i<length.value;i++) {
    for (let j=0;j<length.value;j++) {
      if(matrix[i][j]==1 && visited[i][j]==0 ){
        number += 1
        BFS(i, j)
      }
    }
  }
})  


const test = document.querySelector('.test1 .test2')
console.log(test)