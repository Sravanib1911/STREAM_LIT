import streamlit as st
import pickle
from PIL import Image
import streamlit.components.v1 as components
def main():
    st.title("MY PORTFOLIO ")
    st.sidebar.header("SRAVANI BOMMIREDDYPALLY")
    st.sidebar.image("image/pp1.jpg", use_column_width ='None')




if __name__=='__main__':
    main()

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
  </head>
  <body>
    <div class="p-3 mb-2 bg-light text-dark">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-caret-right-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M12.14 8.753l-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
</svg>
  <a class="navbar-brand" href="#">My Portfolio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
       <li class="nav-item">

       <a class="nav-link" href="#academicdetails">Education</a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="#skills">Skill Set</a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="#certs">Workshops</a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="#project">Hobbies</a>
     </li>
     <li class="nav-item">
       <a class="nav-link" href="#project">contact Me</a>
     </li>
   </ul>
   </nav>
   <hr>

     <h6 class="mt-0">Sravani Bommireddy</h6>
     <button type="button" class="btn btn-dark">BSC-MSCs</button>



 </div>
 <hr>

  <h6>Career Objective </h6>
   <p>Looking for a challenging career to show the best of my professional ability, skills and techniques to
 enhance my knowledge and growth in Electronics and communication industry.</p>
         <hr>
         <div id = "academicdetails">
           <u>
           <h6>Academic Details </h6>
         </u>
         <table class="table table-hover table-white">
           <thead>
             <tr>
               <th scope="col">Qualification</th>
               <th scope="col">College/School</th>
               <th scope="col">GPA/Percentage</th>
               <th scope="col">Passing Year</th>
             </tr>
           </thead>
           <tbody>
               <tr>
                 <th scope="row">BSC-MSCs</th>
                 <td>St.Ann's College for Women.</td>
                 <td>6.7</td>
                 <td>2020</td>
               </tr>
               <tr>
                 <th scope="row">InterMediate</th>
                 <td>Sri Gayatri </td>
                 <td>80%</td>
                 <td>2017</td>
               </tr>
               <tr>
                 <th scope="row">SSC</th>
                 <td>St Anns High School</td>
                 <td>8.3</td>
                 <td>2015</td>
               </tr>
             </tbody>
           </table>
           </div>
           <hr>
           <div id = "skills">
             <u>
               <h6> Skill Set (on scale of 5)</h6>
             </u>

             <ul class="list-group">
         <li class="list-group-item d-flex justify-content-between align-items-center">
           C-programming
           <span class="badge badge-primary badge-pill">4</span>
         </li>
         <li class="list-group-item d-flex justify-content-between align-items-center">
           Java
           <span class="badge badge-primary badge-pill">3</span>
         </li>
         <li class="list-group-item d-flex justify-content-between align-items-center">
           Python
           <span class="badge badge-primary badge-pill">4.5</span>
         </li>
         <li class="list-group-item d-flex justify-content-between align-items-center">
           HTML
           <span class="badge badge-primary badge-pill">4</span>
         </li>
       </ul>
   </ul>
 </div>
 <hr>
 <div id= "worsh">
   <u>
     <h6> Workshops </h6>
   </u>
   <p>
     <ul>
  <li> Presented a project titled Advance Cyber Attacks and its threats 2017.</li>
 <li>  Participated in a workshop on Appreciation and Applications of Data Science, Hyderabad in
 2018.</li>
 <li>  Participated in a workshop Buisness Data Analysis Management and Innovation, Hyderabad
 in 2019.</li>
 <li>  Participated in a National Colloquium on works of a Giant Statistician Prof.C.R.Rao
 AIMSCS, UoH campus, Hyderabad in 2019. </li>
 </ul>
 </div>
 <hr>
 <div id="hob">
   <u>
     <h6>Hobbies</h6>
   </u>
   <p>
     <ul>
 <li> Listening to music </li>
 <li> Watching movies </li>
 <li> Reading books </li>
 </ul>
 </p>
   </div>
   <hr>

 </nav>
 </div>
 <div class="card">
   <button type="button" class="btn btn-light">Contact Me</button>

 <div class="card-body">
 <span style="padding-left:200px">
 <p>Email : sravs.b19@gmail.com
 </p>

 <span style="padding-left:200px">
 <p>
   Mobile no :+91 7287035697
 </p>
 <span style="padding-left:200px">
 <p>
   LinkedIn Profile :sravanibommireddy
 </p>

 </div>
 </div>

   </body>

    """,
    height=2200,
)
