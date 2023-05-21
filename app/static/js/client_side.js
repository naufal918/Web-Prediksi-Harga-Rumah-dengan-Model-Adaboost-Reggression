 $(document).ready(function(){
  
  // -[Animasi Scroll]---------------------------
  
  $(".navbar a, footer a[href='#halamanku']").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
        window.location.hash = hash;
      });
    } 
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });

  
  // -[Prediksi Model]---------------------------
  
  // Fungsi untuk memanggil API ketika tombol prediksi ditekan
  $("#prediksi_submit").click(function(e) {
    e.preventDefault();
	
	// Set data pengukuran bunga iris dari input pengguna
 //  var input_sepal_length = $("#range_sepal_length").val(); 
	// var input_sepal_width  = $("#range_sepal_width").val(); 
	// var input_petal_length = $("#range_petal_length").val(); 
	// var input_petal_width  = $("#range_petal_width").val(); 

    var input_lokasi = $("#lokasi").val(); 
    var input_Kamar_Tidur = $("#kamar_tidur").val(); 
    var input_Tipe_Rumah = $("#tipe_rumah").val();
    var input_Tipe_Listrik = $("#tipe_listrik").val();
    var input_Kamar_Mandi = $("#kamar_mandi").val();

	// Panggil API dengan timeout 1 detik (1000 ms)
    setTimeout(function() {
	  try {
			$.ajax({
			  url  : "/api/prediksi",
			  type : "POST",
			  data : {
          "lokasi" : input_lokasi,
          "kamar_tidur"  : input_Kamar_Tidur,
          "tipe_rumah" : input_Tipe_Rumah,
          "tipe_listrik"  : input_Tipe_Listrik,
          "kamar_mandi"  : input_Kamar_Mandi,
        },
			  success:function(res){
				// Ambil hasil prediksi spesies dan path gambar spesies dari API
				res_data_prediksi   = res['prediksi']
				// res_gambar_prediksi = res['gambar_prediksi']

          console.log(res_data_prediksi)
				// Tampilkan hasil prediksi ke halaman web
			    generate_prediksi(res_data_prediksi); 
			  }
			});
		}
		catch(e) {
			// Jika gagal memanggil API, tampilkan error di console
			console.log("Gagal !");
			console.log(e);
		} 
    }, 1000)
    
  })
    
  // Fungsi untuk menampilkan hasil prediksi model
  function generate_prediksi(data_prediksi) {
    var str="";
    // str += "<img src='" + image_prediksi + "' width=\"200\" height=\"150\"></img>";
    str += "<h3>" +"Harga rumah impian anda adalah sebesar "+ "<br> <br>" +data_prediksi + "</h3>";
    $("#hasil_prediksi").html(str);
  }  
  
})
  
