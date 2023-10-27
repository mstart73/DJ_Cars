 $(document).ready(
function goBack() {
  window.history.back();
};

  function show(a1,a2,a3){

                       $.ajax({
                        url: '/showres',
                        type: 'post',
                        data: {a1: a1},
                        success: function(data){
                            $('.modal-body').html(data);
                            $('.modal-body').append(data.htmlresponse);
                            $('#empModal').modal('show');
                        };
                    });


        });
