<link rel="stylesheet" type="text/css" href="login.css" media="screen"/>

</body>
</html> 

 <div class="Login-box">
  <h2>SignIn</h2>
  <form id = "my_form" action="reg_helper.php" method="post">
    <div class="user-box">
      <input type="text" name="fname" value="Eren">
      <label>First Name</label>
    </div>
    <div class="user-box">
      <input type="text" name="lname" value="Yeagar">
      <label>Last Name</label>
    </div>
    <div class="user-box">
      <input type="email" name="email" value="eren@gmail.com">
      <label>Email</label>
    </div>
    <div class="user-box">
      <input type="password" name="pswd" value="">
      <label>Password</label>
    </div>
    <div class="user-box">
      <input type="date" name="dob">
      <label>Date of Birth</label>
    </div>
    <div class="user-box">
      <!-- Male<input type="radio" name="gender">Female<input type="radio" name="gender"> -->
      <input type = "text" name = "gender" value="">
      <label>Gender</label>
    </div>
    <div class="user-box">
      <input type="text" name="ht" value="">
      <label>Height</label>
    </div>
    <div class="user-box">
      <input type="text" name="wt" value="">
      <label>Weight</label>
    </div>
    <a href="#" onclick="document.getElementById('my_form').submit()" type ="Submit">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <!-- <input type = "Submit" value="SignIn"> -->
      SUBMIT
    </a>
  </form>
</div>
