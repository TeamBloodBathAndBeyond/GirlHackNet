function validateSignIn(){
	var usn = document.forms['logInForm']['accName'].value;
	var pass = document.forms['logInForm']['accPassword'].value;

	if(usn == null || x == ""){
		alert("Please enter your username");
		return false;
	}
	else if(pass == null || pass == ""){
		alert("Please enter a password");
		return false;
	}
}