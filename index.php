<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>GirlHackNet - Home</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="icon" href="imgs/miniLogo.jpg" type="image/jpg" sizes="16x16">
  <link rel="stylesheet" type="text/css" href="css/semantic.min.css">
  <script src="validate.js"></script>
  <script src="js/popup.js"></script>
</head>
<body>
  <div id='header' class='container'>
    <!-- <img src='logo.jpg' id='logo' alt='GirlHackNet'> -->
    <a href='index.html'>
      <img src='imgs/logo.png' id='logo' alt='GirlHackNet'>
    </a>
    <!-- <h1 id='logo'>GirlHackNet</h1> -->
    <!-- <form id='logInForm' action='validated.php' onsubmit="return validate();" method="POST">
      Email: <input type='text' name='accName'></input>
      Password: <input type='password' name='accPassword'></input>
      <button id='signin'>Log In</button>
    </form> -->
    <div class="ui middle aligned very relaxed stackable grid" id='logInForm'>
        <div class="ui form">
          <div class="field">
            <label>Username</label>
            <div class="ui left icon input">
              <input type="text" placeholder="Username">
              <i class="user icon"></i>
            </div>
          </div>
          <div class="field">
            <label>Password</label>
            <div class="ui left icon input">
              <input type="password">
              <i class="lock icon"></i>
            </div>
          </div>
          <div class="ui blue submit button" onclick="return validate();">Login</div>
        </div>
    </div>
      <br>
    </form>
    <button id='signup' onclick='div_show()'>Sign up here!</button>
  </div>
  <div id='main'>
    <div id='pop-up'>
      <form action="localhost:800/newUser/" class='ui form small' id="popForm" method="post" name="form">
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
        <input type="radio" name="c-hs" value="college">College<br>
        <input type="radio" name="c-hs" value="highschool">High School
        <br>
        Skills <span id='skillsSpan' style='font-size: 10pt; font-style: italic;'>ie Java,C++,Python,JSON (No spaces please!)</span>:
        <textarea rows="4" cols="50"></textarea>
        <br>
        <input type='submit' href="javascript:%20check_empty()" class='ui button small' value="Submit">
        <button onclick ="div_hide()">Cancel</button>
      </form>
    </div>
    <div id='imgBanner'>
      <img class="img" src="imgs/coolGals1.jpg">
      <button class='ui button massive' id='signup' onclick='div_show()'>Sign up today!</button>
    </div>
    <div id='info'>
      <p>
        The number of men who attend hackathons is far greater than the number of women.
        This is an undeniable fact. Women have been trying to step back into the field of computing
        but the community is certainly not getting any more estrogen. So we here at BloodBath & Beyond have come up with a solution!
        <strong>GirlHackNet</strong> is a way for women to connect with other women who are attends the same hackathons they are.
        Simply sign up with your name, email, and skill set and you will be on your way to a better hacking experience!
        GirlHackNet's intuitive design will allow all women from all walks of life to find that special group.
        The group in which you will spend blood, sweat, and tears with for 24-36 hours.
        So come join in on the fun!
        </p>
    </div>
  </div>
</body>
</html>
