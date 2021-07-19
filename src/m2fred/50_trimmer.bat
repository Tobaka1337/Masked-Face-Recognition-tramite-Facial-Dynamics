foreach ($dir in $dirs){
cd $dir
$videos = Get-ChildItem "."
foreach ($video in $videos){
cd $video
$counter = 1
$frames = Get-ChildItem "."
foreach ($frame in $frames){
if ($counter -gt 50){
rm $frame.name
}
$counter = $counter + 1
}
cd ..
}
cd ..
}