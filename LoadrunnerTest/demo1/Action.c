Action()
{


	// ����С���ļ��ϵ�
	lr_rendezvous("xiaojiejie");

	lr_start_transaction("big");
	
	lr_start_transaction("getcourse");

	web_reg_find("Text=\"status\": 200",
		LAST);

	web_custom_request("getcoures",
		"URL=http://132.232.44.158:2333/getcoures?pagenum=1",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body=",
		LAST);

	lr_end_transaction("getcourse", LR_AUTO);


	
	lr_start_transaction("login");

	// ��������
	web_reg_save_param("token1",
		"LB=\"token\": \"",
		"RB=\",",
		LAST);

	// ��¼
	web_reg_find("Text=\"status\": 200",
		LAST);
	web_custom_request("login",
		"URL=http://132.232.44.158:2333/login",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"{NewParam}\",\"password\":\"a1234567\"}",
		LAST);

	lr_end_transaction("login", LR_AUTO);

	lr_end_transaction("big", LR_AUTO);


	// ����
	
	web_add_header("token",
		"{token1}");

	lr_start_transaction("fellgoods");
	web_reg_find("Text=\"status\": 200",
		LAST);
	web_custom_request("userfellgoods",
		"URL=http://132.232.44.158:2333/userfellgoods",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"ctype\":\"0\",\"gid\":1}",
		LAST);

	lr_end_transaction("fellgoods", LR_AUTO);


	return 0;
}
