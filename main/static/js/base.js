var app = new Vue({
  el: '#notes_app',
  data: {
  notes: []
  },
  created: function(){
    const vm = this;
    axios.get('/api/notes/')
    .then(function(response){
    vm.notes = response.data
    })
  }
});