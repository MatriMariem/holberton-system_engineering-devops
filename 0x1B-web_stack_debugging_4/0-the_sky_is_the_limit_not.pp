# increase number of open fd
exec { 'fd':
  command =>'sudo sed -i \'s/15/3000/g\' etc/nginx/nginx.conf; sudo service ngix restart',
  path    =>['/bin'],
}
