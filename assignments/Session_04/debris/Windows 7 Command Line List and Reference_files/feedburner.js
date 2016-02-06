function drwidget_feedburner()
{$ezJQuery(window).load(function()
{if($ezJQuery('.feedburnerFeedBlock > ul'))
{if($ezJQuery('.feedburnerFeedBlock > ul').css('margin-left')!=null&&parseInt($ezJQuery('.feedburnerFeedBlock > ul').css('margin-left'))<0)
{$ezJQuery('.feedburnerFeedBlock > ul').css('margin-left','0px');}}});}
var drwidget_feedburner_hasrun=false;drwidget_feedburner();