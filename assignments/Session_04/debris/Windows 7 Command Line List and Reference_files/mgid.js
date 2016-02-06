function drwidget_mgid(){if(ezoFormfactor=='2')
{if($ezJQuery("a[href*='mgid.com']"))
{$ezJQuery("a[href*='mgid.com']").closest("div[id^='MarketGid']").remove();}}
else if(drwidget_mgid_hasrun==false)
{$ezJQuery('div[id^=MarketGid]').each(function(){var this_width=$ezJQuery(this).width();var table_width=$ezJQuery(this).children('table[class^=mctable]').width();if(table_width>this_width)
{var percentage_change=this_width/table_width;$ezJQuery(this).children('table[class^=mctable]').css('width',this_width+'px');$ezJQuery(this).children('table[class^=mctable]').find('*').each(function(){$ezJQuery(this).css('width',($ezJQuery(this).width()*percentage_change)+'px');if(this.nodeName=='IMG')
{$ezJQuery(this).css('height',($ezJQuery(this).height()*percentage_change)+'px');}});}
drwidget_mgid_hasrun=true;})}}
var drwidget_mgid_hasrun=false;drwidget_mgid();