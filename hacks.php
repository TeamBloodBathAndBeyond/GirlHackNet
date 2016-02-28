<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>GirlHackNet</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <link rel="icon" href="imgs/miniLogo.jpg" type="image/jpg" sizes="16x16">


</head>
<body>
  <div id='header'>
    <h1 id='logo'>GirlHackNet</h1>
    <h3>Welcome ADD PERSON'S NAME HERE</h3>
  </div>
  <div id='main'>
    <script>
        $(function() {
          $.ajax({
              url: 'localhost:800/getEvents/',
              type: 'GET',
              success: function(res) {
                  console.log(res);
              },
              //error: function(error) {
                  //console.log(error);
              }
          });
        });
        
    </script>
    
    
    
  </main>
</body>
</html>
