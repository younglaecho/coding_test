function solution(n, lost, reserve) {
  var answer = 0;
  let students =[];
  n = n-lost.length;
  for (let i = 0 ; i < lost.length ; i++) {
      if(reserve.indexOf(lost[i])+1) {
          reserve.splice(reserve.indexOf(lost[i]), 1)
          lost.splice(i, 1)
          n = n + 1; 
          i= i-1;
      }
  }


  for (let i = 0 ; i < lost.length ; i++) {
      if(reserve.indexOf(lost[i]-1)+1) {
          reserve.splice(reserve.indexOf(lost[i]-1), 1) 
          n = n + 1;

          continue;
      } 
      if (reserve.indexOf(lost[i]+1)+1) {
          reserve.splice(reserve.indexOf(lost[i]+1), 1)
          n = n + 1;

          continue;
      } 
  }
  
  return n;
}