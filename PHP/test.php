$hasPermission =true;
$isAuthenticated =false;
canAccessResource =hasPermission && isAuthenticated;
$orVar = $hasPermission || $isAuthenticated;
$noVar = !$hasPermission && $isAuthenticated;

