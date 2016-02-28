<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>GirlHackNet</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" type="text/css" href="skeleton.css">
  <link rel="stylesheet" type="text/css" href="normalize.css">
  <script src="validate.js"></script>
  <script src="js/popup.js"></script>

</head>
<body>

  <?php
      $servername = "localhost";
      $username = "root";
      $password = "girlhack";
      $dbname = "GirlHack_DB";

      $usn = $_POST['accName'];
      $pass = hash('sha256', $_POST['accPassword']);


      $conn = new mysqli($servername, $username, $password, $dbname);
      if($conn->connect_error){
        die("Connection failed: " . $conn->connect_error);
      }
      $sql = "SELECT * from users";
      $result = $conn->query($sql);

      if($result->num_rows > 0){
        while($row = $result->fetch_assoc()){
          if($usn == $row['email'] && $pass = $row['password']){
            $userfname = $row['first_name'];
            echo "<script>alert('Welcome back, $userfname!');</script>";
          }
          else{
            echo "<script>alert('Username or Password is incorrect');</script>";
            echo "<script>document.location.href='index.php'</script>";
          }
        }
      }
      else{
        echo "Register, son.";
      }



  ?>


  <div id='header'>
    <!-- <img src='logo.jpg' id='logo' alt='GirlHackNet'> -->
    <h1 id='logo'>GirlHackNet</h1>
    <form id='logInForm'>
      Email: <input type='text' name='accName'></input>
      Password: <input type='password' name='accPassword'></input>
      <button id='signin'>Log In</button>
    </form>
      
      
      <br>
      <button id='signup' onclick='div_show()'>Sign up here!</button>
  </div>
  <div id='main'>
    <div id='pop-up'>
      <form action="#" id="popForm" method="post" name="form">
        <h2>Join GirlHackNet Today!</h2>
        <hr>
        First Name:
        <input id="fname" name="fname" placeholder="First Name" type="text">
        <br>
        Last Name:
        <input id="lname" name="lname" placeholder="Last Name" type="text">
        <br>
        Password:
        <input id="password" name="password" placeholder="Password" type="password">
        <br>
        Confirm Password:
        <input id="confirm" name="confirm" placeholder="Confirm Password" type="password">
        <br>
        Email:
        <input id="email" name="email" placeholder="Email" type="text">
        <br>
        Bio:
        <textarea rows="4" cols="50"></textarea>
        <br>
        School:
        <input id="school" name="school" placeholder="School" type="text">
        <br>
        Skills ie Java,C++,Python,JSON (No spaces please!):
        <textarea rows="4" cols="50"></textarea>
        <br>
        <input type='submit' href="javascript:%20check_empty()" value="Submit">
        <button onclick ="div_hide()">Cancel</button>
      </form>
    </div>
    <div id='imgBanner'>
      <img class="img" src="imgs/coolGals1.jpg">
    </div>
    <div id='info'>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Fusce ac nibh in tellus sodales accumsan ut sit amet lacus.
        Praesent at sem vel purus iaculis vehicula.
        Donec fermentum quam vitae nunc vulputate accumsan.
        Aenean ullamcorper eros ullamcorper ante fringilla, eget convallis elit pretium.
        Maecenas gravida neque id laoreet consectetur.
        Suspendisse bibendum ex in eleifend finibus.
        In eu enim quis diam mattis tempus vel id odio.
        Duis volutpat ex eget imperdiet vehicula.
        Aliquam eu augue vitae dolor vulputate convallis vel sit amet dui.
        Praesent nec orci aliquet, laoreet neque non, viverra mauris.
        Ut vel elit dignissim felis aliquam bibendum at sit amet mi.
        Maecenas non dui eu arcu lacinia consequat vel eget massa.
        Nunc ac diam vel enim pellentesque pharetra eget non risus.
        Cras a orci sodales, volutpat sapien vel, semper mi.
        Suspendisse scelerisque dolor vel metus ullamcorper, et porttitor elit elementum.
        Sed non ex non ex tincidunt vestibulum.
        Ut feugiat tellus id purus malesuada porta.
      </p>
    </div>
  </div>
</body>
</html>
