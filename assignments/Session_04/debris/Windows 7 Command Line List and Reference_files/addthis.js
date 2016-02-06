function drwidget_addthis(){if(typeof ezExcludeDoctor=='undefined'||typeof ezExcludeDoctor.addthis=='undefined')
{if($ezJQuery('.addthis-smartlayers'))
{$ezJQuery('.addthis-smartlayers').each(function()
{if($ezJQuery(this).css('position')=='fixed'||$ezJQuery(this).css('position')=='static')
{$ezJQuery(this).remove()}});}}}
drwidget_addthis();