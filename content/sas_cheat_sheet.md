Title: Sas cheat sheet
Date: 2018-09-05 21:50
Modified: 2018-08-27 22:13
Category: SAS
Tags: SAS, data_analysis, data_management, gplot, macro, formats
Authors: Simon-M
Summary: A quick reference for common SAS commands

This article is mostly intended as a quick reference for myself.
I cover a very limited subset of uses of various SAS statements and procedures;
those which I have been using more or less repeatedly.

# Importing data:
Libname [documentation](http://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a000214133.htm)

Proc import
[documentation](https://support.sas.com/documentation/cdl/en/proc/61895/HTML/default/viewer.htm#a000308090.htm).

**Remark**: if nothing works, an easy way out is to use the import wizard (`File -> Import Data`).
The generated command can then be saved in a file and inspected or modified.

## CSV Files

```sas
data Table1;
    infile 'C:\path\to\file.csv' encoding='utf-8' delimiter = ';' MISSOVER DSD lrecl=13106 firstobs=2;
       informat Col1 $12. ;
       informat Col2 best32. ;
	   informat Col3 anydtdte12. ;
    input
                Col1  $
                Col2
                Col3  $
    ;
run;
```

## Dbf files
INSEE dataset for instance

```sas
proc import out = Mydata
            datafile = "C:\path\to\file.dbf"
            dbms = dbf replace;
     getdeleted = no;
run;
```

## MS Access databases

```sas
libname accdb "C:\path\to\database.accdb";

data Table1;
	set accdb.table1;
run;

libname accdb clear;
```

## Sas dataset from directory
To import C:\path\to\dir\Table1.sas7bdat.

```sas
libname mydb "C:\path\to\dir";

data Table1;
	set mydb.Table1;
run;

libname mydb clear;
```

# Writing data to a SAS table

```sas
libname mydb "C:\path\to\output_dir";

data mydb.Table1;
	set Table1;
run;

libname mydb clear;
```

# Macros
For someone who has been programming, SAS macros can feel very unintuitive.
They are very much the tell-tale sign that the SAS language has been designed
for statisticians, not for developpers nor computer scientists.
The easiest way to think reason about them is to think about the macro system
of the C preprocessor: SAS macro are mostly working as a text replacement tool,
with some quirks.

## Simplest macro:
Without variables, it is as simple as it gets.

```sas
%macro mymacro();
	proc freq data=Table1;
		table Col1;
	run;
%mend;
%mymacro();
```

## With a loop
Variables, including loop variables, can be accessed with the `&var.` syntax.
The loop syntax is close to for-loops in the usual languages.
[Documentation](https://support.sas.com/documentation/cdl/en/mcrolref/61885/HTML/default/viewer.htm#a000543755.htm).

```sas
%macro mymacro();
	%do i=1 %to 10 %by 2;
		proc freq data=Table1;
			table Col&i.;
		run;
	%end;
%mend;
%mymacro();
```

## With parameters
As previously, we use the `&var.` syntax to access the content of a variable.

```sas
%macro mymacro(tablename);
	%do i=1 %to 10;
		proc freq data=&tablename.;
			table Col&i.;
		run;
	%end;
%mend;
%mymacro(Table1);
```

## Using externally defined macro variables
This is a bit more tricky. Assume you want to loop through the columns in a table.
One way to do it is to define macro variables with convenient names, convenient
meaning indexable.

The  `data _null_` statement allow one to operate without creating a dataset which is
the default behaviour.
The `symput("varname", v)` function assigns a value `v` to a variable called "varname".
In the loop body, we then use the usual `&var.` syntax to access the loop variable value.
However, we are not done: we need to further resolve `Colname&i.` to what we have defined
in the `data` step.
For this, we use the `&&var1&var2.` syntax, meaning "first resolve `var2` to its value, then
resolve the resulting expression.
The process as I figure it out in my mind is the follwing:
`&&Colname&i. -> &&Colname1 -> &Colname1. -> "ID"`.

```sas
data _null_;
    call symput("Colname1", "ID");
    call symput("Colname2", "Group");
    call symput("Colname3", "Status");
run;

%macro mymacro();
	%do i=1 %to 10;
		proc freq data=table1;
			table &&Colname&i.;
		run;
	%end;
%mend;
%mymacro();
```

# Plotting with sgplot
The `sgplot` procedure is fairly easy to use and flexible enough for most purposes.
The only catch which has turned up to be utterly annoying is how the order of categorical
variables is handled. I could not get it right even when sorting the data.
The [axes](http://support.sas.com/documentation/cdl/en/grstatproc/62603/HTML/default/viewer.htm#xaxis-stmt.htm)
command documentation is very useful.

## `Series` for plotting lines
A simple example for the
[series](http://support.sas.com/documentation/cdl/en/grstatproc/62603/HTML/default/viewer.htm#series-stmt.htm)
command.

```sas
proc sgplot data=Table1;
    title "Graph title";
    series x=year y=percent / markers lineattrs=(thickness=2);
    yaxis label = "%" grid;
    xaxis label = "Year";
run;
```

A more complex example with groups, formats, custom colors and a legend.

```sas
proc sgplot data=table1;
    format age age_intervals.;
    styleattrs datacontrastcolors=(blue green orange red);
    title "Graph title";
    series x=year y=percent / group=status;
    yaxis label = "%" grid;
    xaxis label = "Year";
    keylegend / title="Status" position=topright noborder;
run;
```

## `Band` for range of values
This one is very handy for plotting min - max values.

```sas
proc sgplot data=Table1;
   band x=Age lower=Min_size upper=Max_size / group=Status;
   xaxis grid label='Age';
   yaxis grid values=(0 to 45 by 5) VALUESHINT label='Size';
run;
```

## `Vbar` for vertical barplots.
Most of the options for
[vbar](http://support.sas.com/documentation/cdl/en/grstatproc/62603/HTML/default/viewer.htm#vbar-stmt.htm)
are valid for
[hbar](http://support.sas.com/documentation/cdl/en/grstatproc/62603/HTML/default/viewer.htm#hbar-stmt.htm).

```sas
proc sgplot data=table1;
    vbar Year / response=count;
    xaxis label='Year';
    yaxis grid label='Number found';
run;
```

Grouping data:

```sas
proc sgplot data=freq_by_sexe_class;
    vbar Year / response=count group=Status groupdisplay=cluster;
    xaxis label='Year';
    yaxis grid label='Number found';
run;
```

## `Density` to visualize 1-D distributions
Sgplot's
[density](http://support.sas.com/documentation/cdl/en/grstatproc/62603/HTML/default/viewer.htm#density-stmt.htm)
is very simple to use.

```sas
proc sgplot data=table1;
    density Col1 / type=kernel group=Status;
run;
```

A useful alternative is `proc univariate`'s
[histogram statement](http://support.sas.com/documentation/cdl/en/procstat/63104/HTML/default/viewer.htm#procstat_univariate_sect013.htm).

```sas
proc univariate data=table1;
    histogram Col1 / kernel;
run;
```

# Plotting maps
Plotting maps is a bit more involved so I wrote a dedicated article:
[Plotting maps in SAS](plotting-maps-with-sas-labeled-choropleth.html).


# Various tricks using formats
Proc [format](http://support.sas.com/documentation/cdl/en/proc/61895/HTML/default/viewer.htm#a002473464.htm)
can be helpful in various cases beyond the obvious usage. Here are some samples.

## Defining intervals for numerical values

```sas
proc format;
    value age_intervals
        low - < 11 = "Child"
         11 - < 18 = "Teenager"
         18 - high = "Adult"
	;
run;

proc freq data=Table1;
	format age age_intervals.;
	table age;
run;
```

## Getting a summary about missing values

```sas
proc format;
 value $missfmt ' '='Missing' other='Not Missing';
 value  missfmt  . ='Missing' other='Not Missing';
run;

proc freq data=d_table;
    format _CHAR_ $missfmt.;
    tables _CHAR_ / missing missprint nocum nopercent;
    format _NUMERIC_ missfmt.;
    tables _NUMERIC_ / missing missprint nocum nopercent;
run;
```

# Other tips

## Writing the results of a query in a macro variable.

```sas
proc sql;
	select count(*)
	into :air_cnt
	from sashelp.air;
quit;
%put(&air_cnt);
```

## Datalines statement for making dummy datasets

```sas
data dummy;
  input num text $;
  datalines;
1 "one"
2 "two"
3 "three"
;
run;
```
