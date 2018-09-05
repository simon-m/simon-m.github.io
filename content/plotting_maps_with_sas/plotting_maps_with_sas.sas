proc gmap data=maps.france map=maps.france all;
    id id;
    choro lat / nolegend;
run;
quit;

pattern v=e;
proc gmap data=maps.france(obs=1) map=maps.france all;
    id id;
    choro lat / nolegend;
run;
quit;
* Cancel pattern;
pattern;

data map_data;
    set maps.france;
    by Id;
    value = x * y / 10000;
    if first.Id then output;
    keep Id Value;
run;

proc gmap data=map_data map=maps.france;
    id Id;
    choro Value;
run;
quit;

* Average longitude of departements;
proc means data=maps.france mean noprint;
    var x;
    by Id;
    output out=france_dpt_avg_lon mean=x;
run;

* Average latitude of departements;
proc means data=maps.france mean noprint;
    var y;
    by Id;
    output out=france_dpt_avg_lat mean=y;
run;

* Departement centroids;
data france_dpt_proj_centroids;
    merge france_dpt_avg_lon(keep=Id x) 
          france_dpt_avg_lat(keep=Id y);
    by Id;
run;

data pre_labels;
    set france_dpt_proj_centroids;
    retain
    xsys ysys '2'
    hsys      '3'
    position  '5'
    function  'label'
    size      1.5
    style     "'Tahoma/bo'"
    when      'a';
run;

data labels;
	merge pre_labels map_data(keep=Id Value);
	by Id;
	round_value = round(value, 0.1);
	text = put(round_value, 6.1);
run;

proc gmap data=map_data map=maps.france;
	id Id;
	choro Value / annotate=labels;
run;
quit;
