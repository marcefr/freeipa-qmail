# freeipa-qmail

DISCLAIMER: This work is in still-doesn't-work-even-for-me status. Use at your own risk..

Tools and schema to use qmail-ldap against freeipa

To add the necesary schema:
	kinit admin
	ldapmodify -D "cn=directory manager" -W -a -x <qmail.ldif
	sudo systemctl restart ipa
	ipa config-mod --addattr=ipaUserObjectClasses=qmailUser
	ipa config-mod --addattr=ipaUserObjectClasses=qldapAdmin
	ipa config-mod --addattr=ipaGroupObjectClasses=qmailGroup

