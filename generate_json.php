<?php
$base= mysqli_connect("localhost",  "root", "root", "test");

if (mysqli_connect_errno())
  die('Could not connect: ' . mysql_error());

$return_arr = array();

if ($result = mysqli_query( $base, "SELECT * FROM lokasi" )){
    while ($row = mysqli_fetch_assoc($result)) {
    $row_array['id'] = $row['id'];
    $row_array['col1'] = $row['col1'];
    $row_array['col2'] = $row['col2'];

    array_push($return_arr,$row_array);
   }
 }

mysqli_close($base);

echo json_encode($return_arr);

 ?>
