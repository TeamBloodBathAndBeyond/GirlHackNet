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

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT date, link, name, location FROM getEvents";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
      // output data of each row
      while($row = $result->fetch_assoc()) {
        echo "date: " . $row["date"]. " - Link: " . $row["link"]. " Name:" . $row["name"]. " Location:" . $row["location"]. "<br>";
      }
    } else {
      echo "0 results";
    }
    $conn->close();
    ?>
  </main>
</body>
</html>
