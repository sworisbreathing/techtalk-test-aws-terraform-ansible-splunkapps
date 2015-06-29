#!/usr/bin/python

#
# (c) Copyright 2008 NetApp, Inc. The code is provided "as is" without
# support or warranties of any kind.  The user is licensed to use the
# code for any legal purpose.
#

#
# $Id:$	
# 
# Python implementation of NetApp's ONTAP API interfaces.
# 

NaErrors = {
    'EONTAPI_EPERM' : 1,
    'EONTAPI_ENOENT' : 2,
    'EONTAPI_ESRCH' : 3,
    'EONTAPI_EINTR' : 4,
    'EONTAPI_EIO' : 5,
    'EONTAPI_ENXIO' : 6,
    'EONTAPI_E2BIG' : 7,
    'EONTAPI_ENOEXEC' : 8,
    'EONTAPI_EBADF' : 9,
    'EONTAPI_ECHILD' : 10,
    'EONTAPI_EDEADLK' : 11,
    'EONTAPI_ENOMEM' : 12,
    'EONTAPI_EACCES' : 13,
    'EONTAPI_EFAULT' : 14,
    'EONTAPI_ENOTBLK' : 15,
    'EONTAPI_EBUSY' : 16,
    'EONTAPI_EEXIST' : 17,
    'EONTAPI_EXDEV' : 18,
    'EONTAPI_ENODEV' : 19,
    'EONTAPI_ENOTDIR' : 20,
    'EONTAPI_EISDIR' : 21,
    'EONTAPI_EINVAL' : 22,
    'EONTAPI_ENFILE' : 23,
    'EONTAPI_EMFILE' : 24,
    'EONTAPI_ENOTTY' : 25,
    'EONTAPI_ETXTBSY' : 26,
    'EONTAPI_EFBIG' : 27,
    'EONTAPI_ENOSPC' : 28,
    'EONTAPI_ESPIPE' : 29,
    'EONTAPI_EROFS' : 30,
    'EONTAPI_EMLINK' : 31,
    'EONTAPI_EPIPE' : 32,
    'EONTAPI_EDOM' : 33,
    'EONTAPI_ERANGE' : 34,
    'EONTAPI_EAGAIN' : 35,
    'EONTAPI_EINPROGESS' : 36,
    'EONTAPI_EALREADY' : 37,
    'EONTAPI_ENOTSOCK' : 38,
    'EONTAPI_EDESTADDRREQ' : 39,
    'EONTAPI_EMSGSIZE' : 40,
    'EONTAPI_EPROTOTYPE' : 41,
    'EONTAPI_ENOPROTOOPT' : 42,
    'EONTAPI_EPROTONOSUPPORT' : 43,
    'EONTAPI_ESOCKTNOSUPPORT' : 44,
    'EONTAPI_EOPNOTSUPP' : 45,
    'EONTAPI_EPFNOSUPPORT' : 46,
    'EONTAPI_EAFNOSUPPORT' : 47,
    'EONTAPI_EADDRINUSE' : 48,
    'EONTAPI_EADDRNOTAVAIL' : 49,
    'EONTAPI_ENETDOWN' : 50,
    'EONTAPI_ENETUNREACH' : 51,
    'EONTAPI_ENETRESET' : 52,
    'EONTAPI_ECONNABORTED' : 53,
    'EONTAPI_ECONNRESET' : 54,
    'EONTAPI_ENOBUFS' : 55,
    'EONTAPI_EISCONN' : 56,
    'EONTAPI_ENOTCONN' : 57,
    'EONTAPI_ESHUTDOWN' : 58,
    'EONTAPI_ETOOMANYREFS' : 59,
    'EONTAPI_ETIMEDOUT' : 60,
    'EONTAPI_ECONNREFUSED' : 61,
    'EONTAPI_ELOOP' : 62,
    'EONTAPI_ENAMETOOLONG' : 63,
    'EONTAPI_EHOSTDOWN' : 64,
    'EONTAPI_EHOSTUNREACH' : 65,
    'EONTAPI_ENOTEMPTY' : 66,
    'EONTAPI_EPROCLIM' : 67,
    'EONTAPI_EUSERS' : 68,
    'EONTAPI_EDQUOT' : 69,
    'EONTAPI_ESTALE' : 70,
    'EONTAPI_EREMOTE' : 71,
    'EONTAPI_EBADRPC' : 72,
    'EONTAPI_ERPCMSGDENIED' : 73,
    'EONTAPI_EPROGUNAVAIL' : 74,
    'EONTAPI_EPROGMISMATCH' : 75,
    'EONTAPI_EPROCUNAVAIL' : 76,
    'EONTAPI_ENOLCK' : 77,
    'EONTAPI_ENOSYS' : 78,
    'EONTAPI_EFTYPE' : 79,
    'EONTAPI_EMTUTOOBIG' : 80,
    'EONTAPI_EOFFLINE' : 81,
    'EONTAPI_EBADSTREAM' : 82,
    'EONTAPI_EBADSTREAMDIR' : 83,
    'EONTAPI_ELOADCOMPLETE' : 84,
    'EONTAPI_EMOUNTING' : 85,
    'EONTAPI_EWFLUSH' : 99,
    'EONTAPI_EBADPATH' : 100,
    'EONTAPI_EBADCHAR' : 101,
    'EONTAPI_ESHARECONFLICT' : 102,
    'EONTAPI_ELOCKCONFLICT' : 103,
    'EONTAPI_ENOTCOVERED' : 104,
    'EONTAPI_EBADXINODE' : 105,
    'EONTAPI_ENOTXINODE' : 106,
    'EONTAPI_EBADOWNER' : 107,
    'EONTAPI_ERMTWRITELEN' : 108,
    'EONTAPI_EBADRMT' : 109,
    'EONTAPI_EKNOWNBADRMT' : 110,
    'EONTAPI_ERMTEOF' : 111,
    'EONTAPI_EDELPENDING' : 112,
    'EONTAPI_ETRUNCATED' : 113,
    'EONTAPI_EREJECTED' : 114,
    'EONTAPI_EREADONLY' : 115,
    'EONTAPI_EPARTNERREJECT' : 116,
    'EONTAPI_ETOOCOMPLEX' : 117,
    'EONTAPI_EREGX' : 118,
    'EONTAPI_EREGXBADVALUE' : 119,
    'EONTAPI_EPERSISTENCE' : 120,
    'EONTAPI_ESTHREAD' : 121,
    'EONTAPI_EDISABLED' : 122,
    'EONTAPI_ENOTVSCANNED' : 123,
    'EONTAPI_EFABRIC' : 124,
    'EONTAPI_ESYSTEMERR' : 125,
    'EONTAPI_EGSSAPI' : 126,
    'EONTAPI_ERPCGSSSEQNUM' : 127,
    'EONTAPI_EPROXYME' : 128,
    'EONTAPI_ERSRVCONFLICT' : 129,
    'EONTAPI_ERSRVNSUPPORTED' : 130,
    'EONTAPI_ENOQTREE' : 131,
    'EONTAPI_ENOTLOCKED' : 132,
    'EONTAPI_ELOCKCANCELLED' : 133,
    'EONTAPI_ENOSPCSNAP' : 134,
    'EONTAPI_ENOMORESNAPS' : 135,
    'EONTAPI_ERECURSE' : 136,
    'EONTAPI_ERECLAIM' : 137,
    'EONTAPI_EZEROLENREC' : 138,
    'EONTAPI_ENOTFSCREENED' : 139,
    'EONTAPI_EISVDISK' : 140,
    'EONTAPI_EWAFLMSGABORTED' : 141,
    'EONTAPI_EMSGNULLIFY' : 142,
    'EONTAPI_ECOMPRESSCHECK' : 143,
    'EONTAPI_EVOLSMALL' : 144,
    'EONTAPI_EVOLBIG' : 145,
    'EONTAPI_EVOLPAIRED' : 146,
    'EONTAPI_EVOLNOTFLEX' : 147,
    'EONTAPI_EVOLSTALE' : 148,
    'EONTAPI_ENOREG' : 149,
    'EONTAPI_ENOREGKEY' : 150,
    'EONTAPI_ECANNOTDELETE' : 151,
    'EONTAPI_EWORMNOCLOCK' : 152,
    'EONTAPI_EWORMVOLWORM' : 153,
    'EONTAPI_EWORMVOLSLC' : 154,
    'EONTAPI_EWORMVOLNOTWORM' : 155,
    'EONTAPI_EWORMSNAPLOCKED' : 156,
    'EONTAPI_EWORMSNAPRENAME' : 157,
    'EONTAPI_EWORMPERIOD' : 158,
    'EONTAPI_ENOSPCAGGR' : 159,
    'EONTAPI_EVOLOPNOTSUPP' : 160,
    'EVDISK_ERROR_NOT_IMPLEMENTED' : 9000,
    'EVDISK_ERROR_NOT_QTREE_ROOT' : 9001,
    'EVDISK_ERROR_NOT_VDISK_TYPE' : 9002,
    'EVDISK_ERROR_NO_SUCH_INITGROUP' : 9003,
    'EVDISK_ERROR_INITGROUP_EXISTS' : 9004,
    'EVDISK_ERROR_NOT_VALID_FC_WWN' : 9005,
    'EVDISK_ERROR_NOT_VALID_ISCSI_NAME' : 9006,
    'EVDISK_ERROR_NODE_NOT_IN_INITGROUP' : 9007,
    'EVDISK_ERROR_INITGROUP_HAS_NODE' : 9008,
    'EVDISK_ERROR_LUN_MAPPING_CONFLICT' : 9009,
    'EVDISK_ERROR_INITGROUP_WRONG_TYPE' : 9010,
    'EVDISK_ERROR_NO_SUCH_ATTRIBUTE' : 9011,
    'EVDISK_ERROR_VDISK_EXISTS' : 9012,
    'EVDISK_ERROR_VDISK_EXPORTED' : 9013,
    'EVDISK_ERROR_VDISK_NOT_ENABLED' : 9014,
    'EVDISK_ERROR_VDISK_NOT_DISABLED' : 9015,
    'EVDISK_ERROR_NO_SUCH_LUNMAP' : 9016,
    'EVDISK_ERROR_NO_SUCH_VDISK' : 9017,
    'EVDISK_ERROR_NOT_IN_SAME_QTREE' : 9018,
    'EVDISK_ERROR_SOURCE_IS_VDISK' : 9019,
    'EVDISK_ERROR_NO_SUCH_DIRECTORY' : 9020,
    'EVDISK_ERROR_INVALID_SNAPSHOT_PATH' : 9021,
    'EVDISK_ERROR_NOT_IN_SAME_VOLUME' : 9022,
    'EVDISK_ERROR_INITGROUP_HAS_VDISK' : 9023,
    'EVDISK_ERROR_INITGROUP_HAS_LUN' : 9024,
    'EVDISK_ERROR_INITGROUP_MISSING_ARGS' : 9025,
    'EVDISK_ERROR_INITGROUP_INVALID_ATTR_TYPE' : 9026,
    'EVDISK_ERROR_INITGROUP_INVALID_ATTR_VALUE' : 9027,
    'EVDISK_ERROR_NO_EXPORTED_VDISK_SHARE_WRITE' : 9028,
    'EVDISK_ERROR_INITGROUP_MAPS_EXIST' : 9029,
    'EVDISK_ERROR_VOLUME_NOT_SPACE_RESERVED' : 9030,
    'EVDISK_ERROR_SNAPSHOT_FILE_NOT_VDISK' : 9031,
    'EVDISK_ERROR_NITGROUP_INVALID_ATTR_VALUE_OS_TYPE' : 9032,
    'EVDISK_ERROR_MUST_SPECIFY_F_FLAG' : 9033,
    'EVDISK_ERROR_SIZE_TOO_LARGE' : 9034,
    'EVDISK_ERROR_RESIZE_TOO_LARGE' : 9035,
    'EVDISK_ERROR_NO_SUCH_VOLUME' : 9036,
    'EVDISK_ERROR_USER_ABORT_ACTION' : 9037,
    'EVDISK_ERROR_CLONING' : 9038,
    'EVDISK_ERROR_INITIATOR_HAS_VDISK' : 9039,
    'EVDISK_ERROR_FILE_IS_SPC_RESERVED' : 9040,
    'EVDISK_ERROR_SIZE_TOO_SMALL' : 9041,
    'EVDISK_ERROR_SIZE_UNCHANGED' : 9042,
    'EVDISK_ERROR_NO_SUCH_SNAPSHOT' : 9043,
    'EVDISK_ERROR_IGROUP_NOT_THROTTLED' : 9044,
    'EVDISK_ERROR_IGROUP_ALREDY_THROTTLED' : 9045,
    'EVDISK_ERROR_THROTTLE_TOO_MUHC' : 9046,
    'EVDISK_ERROR_THROTTLE_BEING_DELETED' : 9047,
    'EVDISK_ERROR_NO_SUCH_CLONE' : 9048,
    'EVDISK_ERROR_NO_ISCSI_THROTTLES' : 9049,
    'EVDISK_ERROR_INVALID_ATTR_MODE_VALUE' : 9050,
    'EVDISK_ERROR_INITGROUP_MEMBER_CONFLICTING_OS_TYPES' : 9051,
    'EVDISK_ERROR_INITGROUP_SET_TYPE_CONFLICT' : 9052,
    'EVDISK_ERROR_INITGROUP_MEMBER_VSA_MIXED' : 9053,
    'EVDISK_ERROR_INITGROUP_SET_VSA_CONFLICT' : 9054,
    'EVDISK_ERROR_RESIZE_FIXES_NOT_GEOM_ALIGNED' : 9055,
    'EVDISK_ERROR_RESIZE_VLD_TYPE_LUN_FIXES' : 9056,
    'EVDISK_ERROR_RESIZE_IMGAG_TYPE_LUN_FIXES' : 9057,
    'EVDISK_ERROR_INITGROUP_F_FLAG_REQUIRED' : 9058,
    'EVDISK_ERROR_USE_PARTNER_NOT_APPLICABLE' : 9059,
    'EVDISK_ERROR_RESTORE_WALKOVER_EACHOTHER' : 9060,
    'EVDISK_ERROR_VOLUME_SPARSE' : 9061,
    'EVDISK_ERROR_DESTROY_LUN_BUSY' : 9062,
    'EVDISK_ERROR_CANT_CREATE_INITGROUP_FILE' : 9063,
    'EVDISK_ERROR_CANT_WRITE_INITGROUP_FILE' : 9064,
    'EVDISK_ERROR_CANT_RENAME_INITGROUP_FILE' : 9065,
    'EVDISK_ERROR_CANT_CREATE_VFILER_SHADOW_INITGROUP_FILE' : 9066,
    'EVDISK_ERROR_CANT_WRITE_VFILER_SHADOW_INITGROUP_FILE' : 9067,
    'EVDISK_ERROR_CANT_RENAME_VFILER_SHADOW_INITGROUP_FILE' : 9068,
    'EVDISK_ERROR_INITGROUP_TOO_MANY_NODENAMES' : 9069,
    'EVDISK_ERROR_LUN_MISSING_FROM_SNAPSHOT' : 9070,
    'EVDISK_ERROR_SNAPVALIDATOR_ERROR' : 9071,
    'EVDISK_ERROR_PARTNER_HAS_LUN' : 9072,
    'EVDISK_ERROR_PARTNER_NOT_REACHABLE' : 9073,
    'EVDISK_ERROR_PORTSET_NO_SUCH_SET' : 9074,
    'EVDISK_ERROR_PORTSET_ALREADY_EXIST' : 9075,
    'EVDISK_ERROR_PORTSET_HAS_PORT' : 9076,
    'EVDISK_ERROR_PORTSET_INVALID_PORT_NAME' : 9077,
    'EVDISK_ERROR_PORTSET_TOO_MANY_PORTS' : 9078,
    'EVDISK_ERROR_PORTSET_WRONG_TYPE' : 9079,
    'EVDISK_ERROR_INITGROUP_ALREADY_BOUND' : 9080,
    'EVDISK_ERROR_INITGROUP_NOT_BOUND' : 9081,
    'EVDISK_ERROR_INITGROUP_EMPTY_PSET_BIND' : 9082,
    'EVDISK_ERROR_PORTSET_NO_SUCH_PORT' : 9083,
    'EVDISK_ERROR_PORTSET_NO_SUCH_FILER_NAME' : 9084,
    'EVDISK_ERROR_PARTNER_HAS_DIFFERENT_OS_TYPE' : 9085,
    'EVDISK_ERROR_PARTNER_HAS_DIFFERENT_VSA_SETTING' : 9086,
    'EVDISK_ERROR_PORTSET_CANT_CREATE_FILE' : 9087,
    'EVDISK_ERROR_PORTSET_CANT_WRITE_FILE' : 9088,
    'EVDISK_ERROR_PORTSET_CANT_READ_FILE' : 9089,
    'EVDISK_ERROR_PORTSET_CANT_OPEN_FILE' : 9090,
    'EVDISK_ERROR_LUN_TOO_LARGE' : 9091,
    'EVDISK_ERROR_PORTSET_IC_DOWN' : 9092,
    'EVDISK_ERROR_CLONE_NOT_SPLITTING' : 9093,
    'EVDISK_ERROR_LUN_HAS_NO_SERIAL_NO' : 9095,
    'EVDISK_ERROR_PORTSET_THROTTLE_EXCEEDED' : 9096,
    'EVDISK_ERROR_PORTSET_CANT_DESTROY_BOUND_PORTSET' : 9097,
    'EVDISK_ERROR_CFMODE_MISMATCH' : 9098,
    'EVDISK_ERROR_PORTSET_NOT_VALID_CFMODE' : 9099,
    'EVDISK_ERROR_CANNOT_CHANGE_SPCRES_DURING_SPLIT' : 9100,
    'EVDISK_ERROR_INITGROUP_BIND_WRONG_TYPE' : 9101,
    'EVDISK_ERROR_DB_BAD_INDEX' : 9102,
    'EVDISK_ERROR_DB_NO_SUCH_DATABASE' : 9103,
    'EVDISK_ERROR_ALUA_NOT_SUPPORTED_ON_ISCSI' : 9104,
    'EVDISK_ERROR_ALUA_NOT_SUPPORTED_ON_CFMODE' : 9105,
    'EAPIERROR' : 13001,
    'EAPIAUTHENTICATION' : 13002,
    'EAPIPRIVILEGE' : 13003,
    'EAPIPRIVILEDGE' : 13003,
    'EAPIEXCEPTION' : 13004,
    'EAPINOTFOUND' : 13005,
    'EAPIMISSINGARGUMENT' : 13006,
    'EAPINOTIMPLEMENTED' : 13007,
    'EAPILICENSE' : 13008,
    'EAPIINDEXTOOLARGE' : 13009,
    'EAPIUNSUPPORTEDVERSION' : 13010,
    'EAPITRANSMISSION' : 13011,
    'EOPNOTSUPPORTED' : 13012,
    'EALREADYSTARTED' : 13013,
    'ENOTSTARTED' : 13014,
    'ESERVICENOTSTOPPED' : 13015,
    'ENOTWHILEWAITINGFORGIVEBACK' : 13016,
    'ENOTINMAINTMODE' : 13017,
    'ENOTINREADONLYMODE' : 13018,
    'EAPITOOMANYENTRIES' : 13019,
    'ESNAPSHOTEXISTS' : 13020,
    'ESNAPSHOTDOESNOTEXIST' : 13021,
    'ESNAPSHOTTOOMANY' : 13022,
    'ESNAPSHOTNOTALLOWED' : 13023,
    'ESNAPSHOTBUSY' : 13024,
    'ESNAPSHOTNOSPACE' : 13025,
    'EDUPLICATEDSID' : 13026,
    'EINVALIDDSID' : 13027,
    'EINVALIDMSID' : 13028,
    'EAMBIGUOUS_DSID' : 13029,
    'EVOLUMESNAPRESTOREERROR' : 13038,
    'EVOLUMEQUIESCED' : 13039,
    'EVOLUMEDOESNOTEXIST' : 13040,
    'EVOLUMEMOUNTING' : 13041,
    'EVOLUMEOFFLINE' : 13042,
    'EVOLUMEREADONLY' : 13043,
    'EVOLUMENAMEINVALID' : 13044,
    'EVOLUMERGSIZEINVALID' : 13045,
    'EVOLUMELANGUAGEINVALID' : 13046,
    'EVOLUMEDISKSIZEINVALID' : 13047,
    'EVOLUMEDISKDUP' : 13048,
    'EVOLUMERGINVALID' : 13049,
    'EQUOTAPARSEERROR' : 13050,
    'EQUOTAINVALID' : 13051,
    'EQUOTAEXISTS' : 13052,
    'EQUOTADOESNOTEXIST' : 13053,
    'EQUOTADIRECTIVE' : 13054,
    'EAPI_CONNECTION' : 13055,
    'EAPI_CONNECTION_DROPPED' : 13056,
    'EAPI_RECEPTION' : 13057,
    'EVOL_NOT_OFFLINE' : 13058,
    'EVOL_NOT_RESTRICTED' : 13059,
    'EVOL_ONLINE' : 13060,
    'EVOL_RESTRICTED' : 13061,
    'EVOL_SPACE_FOR_GUARANTEE' : 13062,
    'EVOL_TOO_MANY' : 13063,
    'EVFILEROPNOTALLOWED' : 13070,
    'EVFILERNOTFOUND' : 13071,
    'EVFILEROPNOTCOMPLETED' : 13072,
    'EIPSPACENOTFOUND' : 13073,
    'EQTREEEXISTS' : 13080,
    'EQTREENOTOWNER' : 13081,
    'EQTREEMAX' : 13082,
    'ECMSINVALIDREQUEST' : 13090,
    'ECMSNOTENABLED' : 13091,
    'ECMSPROCESSINGERROR' : 13092,
    'ESNAPMIRROROFF' : 13100,
    'ESNAPMIRRORPARSERERROR' : 13101,
    'ESNAPMIRRORERROR' : 13102,
    'EISCSISECINVALIDAUTHTYPE' : 13109,
    'EISCSISECINVALIDINPUTERROR' : 13110,
    'EISCSISECPROCESSINGERROR' : 13111,
    'EISCSISECINITNOTFOUNDERROR' : 13112,
    'EFILENOTFOUND' : 13113,
    'EINTERNALERROR' : 13114,
    'EINVALIDINPUTERROR' : 13115,
    'ESETSPCRESERROR' : 13116,
    'EADAPTERNOTFOUND' : 13122,
    'EADAPTERPARTNER' : 13123,
    'EADAPTERINVALIDTYPE' : 13125,
    'ENOADAPTERPARTNER' : 13126,
    'ENOVIRTUALADAPTERS' : 13127,
    'ENOTCLUSTERED' : 13128,
    'ECLUSTERED' : 13129,
    'EDISKNOTFOUND' : 13150,
    'ESWAPINPROGRESS' : 13151,
    'ENOTDISKOWNER' : 13152,
    'EDISKINRAIDZEROVOL' : 13153,
    'EDISKISSPARE' : 13154,
    'EVOLUMEPLEXINVALID' : 13155,
    'EVOLUMEINUSE' : 13156,
    'EVOLUMENOTONLINE' : 13157,
    'EVOLUMEBUSY' : 13158,
    'EVOLUMECIFSTERMINATE' : 13159,
    'EVOLUMECREATING' : 13160,
    'ECLIENTSTATSVFILER' : 13161,
    'ECLIENTSTATSNOTENABLED' : 13162,
    'ENOACTIVECLIENTS' : 13163,
    'ECIFSNOTCONFIGURED' : 13164,
    'EDNSNOTENABLED' : 13165,
    'EHOSTNOTFOUND' : 13166,
    'ELDAPSVRNOTFOUND' : 13167,
    'ESVCDISABLED' : 13200,
    'ESVCNOTAVAIL' : 13201,
    'ESHAREACCESSDENIED' : 13202,
    'ESHAREEXISTS' : 13203,
    'ESHARETOOMANY' : 13204,
    'ECIFSSHARINGVIOLATION' : 13210,
    'ESANOWNNOTENABLED' : 13210,
    'EINVALIDHOST' : 13211,
    'EINVALIDOWNERID' : 13212,
    'EINVALIDOWNER' : 13213,
    'EINVALIDPASSWORD' : 13214,
    'EEXPORTSINCOMPATIBLE' : 13215,
    'EINODENUMBERTOOSMALL' : 13216,
    'EINODENUMBERTOOLARGE' : 13217,
    'EINVALIDINODE' : 13218,
    'EINELIGIBLEINODE' : 13219,
    'EPARENTINFONOTLOADED' : 13220,
    'EI2PNOTENABLED' : 13221,
    'EVV_COMMON' : 13222,
    'ECIFS_LOGIN_FAILED' : 13250,
    'ECIFS_BIND_FAILED' : 13251,
    'ECIFS_DNS_REQUIRED' : 13252,
    'ECIFS_KRB_CONFLICT' : 13253,
    'ECIFS_AD_CLOCK_SKEW' : 13254,
    'ECIFS_AD_RESET_REQUIRED' : 13255,
    'ECIFS_LIST_UNAVAILABLE' : 13256,
    'ECIFS_DC_CONNECT_FAILED' : 13257,
    'ECIFS_HAVE_SESSION_SCOPED_LOCKS' : 13258,
    'ECIFS_PASSWD_AND_GROUP_REQUIRED' : 13259,
    'ECIFS_SETUP_CANNOT_WRITE' : 13260,
    'EEMS_INVOKE_FAILED' : 13301,
    'EEMS_INVOKE_BAD_PARAM' : 13303,
    'EEMS_INVOKE_ID_BAD' : 13310,
    'EEMS_INVOKE_SEVERITY_REQUIRED' : 13311,
    'EEMS_INVOKE_SEVERITY_INVALID' : 13312,
    'EEMS_INVOKE_SEVERITY_NOT_VARIABLE' : 13313,
    'EEMS_INVOKE_PARAMS_INSUFFICIENT' : 13314,
    'EEMS_INVOKE_VERSION_INVALID' : 13315,
    'EEMS_INVOKE_SUPRESS_DUP' : 13316,
    'EEMS_INVOKE_SUPRESS_TIMER' : 13317,
    'EEMS_INVOKE_NVRAM_TOO_BIG' : 13318,
    'EEMS_INVOKE_QUEUE_FULL' : 13319,
    'EREALLOCATE_EXISTS' : 13501,
    'EREALLOCATE_BADPATH' : 13502,
    'EREALLOCATE_NOMEM' : 13503,
    'EREALLOCATE_NOSCAN' : 13504,
    'EREALLOCATE_BADVOL' : 13505,
    'EREALLOCATE_READONLY' : 13506,
    'EREALLOCATE_BADSCHED' : 13507,
    'EREALLOCATE_OFF' : 13508,
    'EREALLOCATE_SNAPSHOT' : 13509,
    'EDISKNOTSPARE' : 13510,
    'EDISKTOOSMALL' : 13511,
    'ERAIDGROUPDEGRADED' : 13512,
    'ESAVECOREDISK' : 13513,
    'EINVALIDSTATE' : 13514,
    'ECANT_USE_ALL_DISKS' : 13515,
    'ENPMINVPLOC' : 13600,
    'ENPMNOPKG' : 13601,
    'ENPMNOMETA' : 13602,
    'ENPMERXMETA' : 13603,
    'EINCRCOPYFAILED' : 13604,
    'EINCRCOPYOPNOTFOUND' : 13605,
    'EINCRCOPYINVALIDUUID' : 13606,
    'EINCRCOPYINVALIDOP' : 13607,
    'EINCRCOPYNOMEM' : 13608,
    'EINCRCOPYINVALIDINPUT' : 13609,
    'EINCRCOPYINVALIDOPTYPE' : 13610,
    'EINCRCOPYDUPLICATESESSION' : 13611,
    'EINCRCOPYNOTSUPPORT' : 13612,
    'EINCRCOPYVOLOFFLINE' : 13613,
    'EINCRCOPYVOLNOTFOUND' : 13614,
    'EINCRCOPYSNAPCREATIONFAIL' : 13615,
    'EINCRCOPYSNAPSHOTEXIST' : 13616,
    'EINCRCOPYNOSTREAMESTABLISHED' : 13617,
    'EINCRCOPYAGAIN' : 13618,
    'EINCRCOPY_CSM_CALL_FAIL' : 13619,
    'EINCRCOPY_CSM_SEND_FAIL' : 13620,
    'EINCRCOPY_CSM_CANT_GET_SESSION' : 13621,
    'EINCRCOPY_CSM_CANT_REGISTER_SENDCB' : 13622,
    'EDSIDPARSEERROR' : 13623,
    'EINCRCOPY_SET_INCORE_QUIESCE_VOL_FAIL' : 13624,
    'EINCRCOPY_UNSET_INCORE_QUIESCE_VOL_FAIL' : 13625,
    'EINCRCOPY_SET_ONDISK_QUIESCE_VOL_FAIL' : 13626,
    'ECGERROR' : 13700,
    'ECGSNAPERR' : 13701,
    'ECGOFF' : 13702,
    'ECHARMAP_INVALID' : 13800,
    'ECHARMAP_NO_PERSIST' : 13801,
    'ETOERRMIN' : 13900,
    'ESERVICENOTINITIALIZED' : 13901,
    'ESERVICENOTLICENSED' : 13902,
    'ESERVICENOTENABLED' : 13903,
    'EMBOXDEGRADED' : 13904,
    'EMBOXUNKNOWN' : 13905,
    'EMBOXVERSIONMISMATCH' : 13906,
    'EPARTNERDISABLEDTO' : 13907,
    'EOPERATORDENY' : 13908,
    'ENVRAMSIZEMISMATCH' : 13909,
    'EVERSIONMISMATCH' : 13910,
    'EINTERCONNECTERROR' : 13911,
    'EPARTNERBOOTING' : 13912,
    'ESHELFHOT' : 13913,
    'EPARTNERREVERT' : 13914,
    'ELOCALREVERT' : 13915,
    'EPARTNERTRYINGTAKEOVER' : 13916,
    'ETAKEOVERINPROGRESS' : 13917,
    'EHALTNOTAKEOVER' : 13918,
    'EUNSYNCNVRAM' : 13919,
    'EUNKNOWNTAKEOVERERROR' : 13920,
    'EWAITINGFORPARTNER' : 13921,
    'ELOWMEMORY' : 13922,
    'EHALTING' : 13923,
    'EMBOXUNCERTAIN' : 13924,
    'ENOAUTOTAKEOVER' : 13925,
    'EPARTNERNOTWAITING' : 13926,
    'ENOAGGRS' : 13927,
    'ENOTHINGTOTAKEOVER' : 13945,
    'ESENDHOMEINPROGRESS' : 13946,
    'ENVRAMDOWN' : 13947,
    'EINTERCONNECTRESET' : 13948,
    'EBADOPTIONS' : 13949,
    'ENOTHALTED' : 13950,
    'EREVERTINPROGRESS' : 13951,
    'ESERVICEENABLED' : 13952,
    'EINTAKEOVER' : 13953,
    'ETOERRMAX' : 13954,
    'EINVALIDRESERVATION' : 14000,
    'ENODISKSFOUND' : 14001,
    'EMUSTBEINMAINTMODE' : 14002,
    'EFILEEXISTS' : 14003,
    'EJUNCTIONEXISTS' : 14004,
    'EJUNCTIONDOESNOTEXIST' : 14005,
    'EBADFILELENGTH' : 14006,
    'EFILER_NOT_HEALTHY' : 14007,
    'EBADCOREID' : 14100,
    'ECOREDUMPBUSY' : 14101,
    'ECOREDUMPNOTINITIALIZED' : 14102,
    'ESESNOTREADY' : 14200,
    'ESESBUSY' : 14201,
    'ERDB_HA_SF_NOT_INITIALIZED' : 14300,
    'ERDB_HA_ID_MISMATCH' : 14301,
    'ERDB_HA_CONFIGURED' : 14302,
    'ERDB_HA_PARTIALLY_CONFIGURED' : 14303,
    'ERDB_HA_NOT_CONFIGURED' : 14304,
    'ERDB_HA_CONFIG_UUID_MISMATCH' : 14305,
    'ERDB_HA_CANNOT_EXIT_CONFIG' : 14306,
    'ERDB_HA_IO_ERROR' : 14307,
    'ERDB_HA_INVALID_SLOT' : 14308,
    'ERDB_HA_OLD_COOKIE' : 14309,
    'ERDB_HA_INVALID_INPUT' : 14310,
    'ERDB_HA_FAILURE' : 14311,
    'ERDB_HA_ILLEGAL_SLOT_CONTENT' : 14312,
    'ERDB_HA_SLOT_UUID_MISMATCH' : 14313,
    'EFIJIINVALID' : 14401,
    'EFIJIINVALIDEXPR' : 14402,
    'EFIJINOFILTER' : 14403,
    'EFIJIMAXFILTERS' : 14404,
    'ENFS_CLIENT_STATS_NOT_ENABLED' : 14424,
    'ESNAPVAULTERR' : 14450,
    }