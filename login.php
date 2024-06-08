<link rel="stylesheet" type="text/css" href="login.css" media="screen"/>

</body>
</html> 

 <div class="login-box">
  <h2>Login</h2>
  <!-- <h2>New User</h2> -->
  <form id = "my_form" action="login_helper.php" method="post">
    <div class="user-box">
      <input type="text" name="email" value="" requuired>
      <label>Email</label>
    </div>
    <div class="user-box">
      <input type="password" name="pswd" value="" required>
      <label>Password</label>
    </div>
    <a href = "#" onclick="document.getElementById('my_form').submit()" type = "Submit">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      LogIn
      <!-- <input type = "Submit" value="Login"> -->
    </a>
   <!--  <a href="register.php">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      New User? Signup
    </a> -->
  </form>
<a href="register.php">
New User? Signup
</a>
</div>
