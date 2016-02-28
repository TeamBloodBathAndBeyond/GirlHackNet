<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>GirlHackNet</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="icon" href="imgs/miniLogo.jpg" type="image/jpg" sizes="16x16">


</head>
<body>
  <div id='header'>
    <h1 id='logo'>GirlHackNet</h1>
    <h3>Welcome  ADD PERSON'S NAME HERE</h3>
  </div>
  <div id='main'>
    <?php
    $servername = "localhost";
    $username = "root";
    $password = "girlhack";
    $dbname = "GirlHack_DB";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if($conn->connect_error){
      die("Connection failed: " . $conn->connect_error);
    }
    $hackathons = mysql_query(getEvents);
    ?>
  </main>
</body>
</html>
