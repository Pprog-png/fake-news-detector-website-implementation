button = document.getElementById("button")
document.getElementById('button').onclick = function() {
if (document.getElementById("input").value != ""){

  load = document.getElementById("loading")
  load.classList.remove("hidden")
  setTimeout(() => {
    const options = {
  method: 'GET',
};

function withresult(data){
  result = data['data'][1]
  if( result == 0){
    document.getElementById("back").classList.add("false")
    document.getElementById("back").classList.remove("true")
    document.getElementById("result").innerHTML = "The news is Fake"
  }else if (result == 1){
    document.getElementById("back").classList.add("true")
    document.getElementById("back").classList.remove("false")
    document.getElementById("result").innerHTML = "The news is True"
  }
  res = data['search']['s']
  container_news = document.getElementById("news-container")
  container_news.innerHTML = ''
  for (i = 0; i <res.length; i++){
    para = document.createElement("div")
    para.classList.add("block")
    ln = res[i]['link'].slice(0,50)+"..."
    para.innerHTML = '<div class="title">'+res[i]['title']+'</div><div class="snippet">'+res[i]['snippet']+'</div><a target="_blank" href="'+res[i]['link']+'">'+ln+'</a>'
    container_news.appendChild(para)
  }
}
fetch('/api'+"?data="+document.getElementById("input").value, options)
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
})
.then(data => {
  load = document.getElementById("loading")
  load.classList.add("hidden")
  withresult(data)
})
.catch(error => {
  console.error('Fetch error:', error);
});
}, 1000);
}
}