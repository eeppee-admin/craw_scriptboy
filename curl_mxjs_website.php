<?php
$imcysHtml = file_get_contents("https://imcys.com");

preg_match_all("/title=\"(.*)\" class=/i", $imcysHtml, $title_matches);
preg_match_all("/alt=\"(.*)\" title/i", $imcysHtml, $image_matches);
preg_match_all("/<a href=\"(.*)\" rel=/i", $imcysHtml, $url_matches);

$title_array = $title_matches[1];
$image_array = $image_matches[1];
$url_array = $url_matches[1];

$json = array();

for ($i = 0; $i < sizeof($title_array); $i++) {
    $json[$i]["title"] = $title_array[$i];
    $json[$i]["image"] = $image_array[$i];
    $json[$i]["url"] = $url_array[$i];
}

echo json_encode($json, true);