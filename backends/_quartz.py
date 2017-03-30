from ctypes import *
from ctypes import util

from objc_util import *

if sizeof(c_size_t) == 8:
    CGFloat = c_double
else:
    CGFloat = c_float

quartz = c

CGBitmapInfo = c_uint32  # CGImage.h
CGPathDrawingMode = c_int32  # CGContext.h
CGColorRenderingIntent = c_int32  # CGColorSpace.h

class CGPoint(Structure):
    _fields_ = [
        ('x', CGFloat),
        ('y', CGFloat)
    ]

class CGSize(Structure):
    _fields_ = [
        ('width', CGFloat),
        ('height', CGFloat)
    ]

class CGRect(Structure):
    _fields_ = [
        ('origin', CGPoint),
        ('size', CGSize)
    ]

##############
# Constants
#

kCGColorSpaceSRGB = ObjCInstance(c_void_p.in_dll(quartz, 'kCGColorSpaceSRGB'))
kCGImageAlphaPremultipliedLast = 1
kCGPathFillStroke = 3
kCGRenderingIntentDefault = 0

##############
# Functions

quartz.CFURLCreateFromFileSystemRepresentation.argtypes = [c_void_p, c_char_p, c_size_t, c_bool]

quartz.CGBitmapContextCreate.restype = c_void_p
quartz.CGBitmapContextCreate.argtypes = [c_void_p, c_size_t, c_size_t, c_size_t, c_size_t, c_void_p, CGBitmapInfo]

quartz.CGImageSourceCreateImageAtIndex.restype = c_void_p
quartz.CGImageSourceCreateImageAtIndex.argtypes = [c_void_p, c_size_t, c_void_p]

quartz.CGColorSpaceCreateDeviceRGB.restype = c_void_p
quartz.CGColorSpaceCreateDeviceRGB.argtypes = []

quartz.CGColorSpaceCreateWithName.restype = c_void_p
quartz.CGColorSpaceCreateWithName.argtypes = [c_void_p]

quartz.CGContextAddEllipseInRect.argtypes = [c_void_p, CGRect]  # Double check

quartz.CGContextAddPath.argtypes = [c_void_p, c_void_p]

quartz.CGContextAddRect.argtypes = [c_void_p, CGRect]  # Double check

quartz.CGContextDrawImage.argtypes = [c_void_p, CGRect, c_void_p]  # Double check

quartz.CGContextDrawPath.argtypes = [c_void_p, CGPathDrawingMode]

quartz.CGContextSetLineWidth.argtypes = [c_void_p, CGFloat]

quartz.CGContextSetRGBFillColor.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]

quartz.CGContextSetRGBStrokeColor.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]

quartz.CGDataProviderCreateWithFilename.restype = c_void_p
quartz.CGDataProviderCreateWithFilename.argtypes = [c_char_p]

quartz.CGImageCreateWithJPEGDataProvider.restype = c_void_p
quartz.CGImageCreateWithJPEGDataProvider.argtypes = [c_void_p, CGFloat, c_bool, CGColorRenderingIntent]

quartz.CGImageCreateWithPNGDataProvider.restype = c_void_p
quartz.CGImageCreateWithPNGDataProvider.argtypes = [c_void_p, CGFloat, c_bool, CGColorRenderingIntent]

quartz.CGImageDestinationAddImage.argtypes = [c_void_p, c_void_p, c_void_p]

quartz.CGImageDestinationFinalize.restype = c_bool
quartz.CGImageDestinationFinalize.argtypes = [c_void_p]

quartz.CGImageGetHeight.restype = c_size_t
quartz.CGImageGetHeight.argtypes = [c_void_p]

quartz.CGImageGetWidth.restype = c_size_t
quartz.CGImageGetWidth.argtypes = [c_void_p]

quartz.CGPathAddLineToPoint.argtypes = [c_void_p, c_void_p, CGFloat, CGFloat]

quartz.CGPathCreateMutable.restype = c_void_p

quartz.CGPathMoveToPoint.argtypes = [c_void_p, c_void_p, CGFloat, CGFloat]

CFURLCreateFromFileSystemRepresentation = quartz.CFURLCreateFromFileSystemRepresentation
CGBitmapContextCreate = quartz.CGBitmapContextCreate
CGBitmapContextCreateImage = quartz.CGBitmapContextCreateImage
CGColorSpaceCreateDeviceRGB = quartz.CGColorSpaceCreateDeviceRGB
CGColorSpaceCreateWithName = quartz.CGColorSpaceCreateWithName
CGContextAddEllipseInRect = quartz.CGContextAddEllipseInRect
CGContextAddPath = quartz.CGContextAddPath
CGContextAddRect = quartz.CGContextAddRect
CGContextDrawImage = quartz.CGContextDrawImage
CGContextDrawPath = quartz.CGContextDrawPath
CGContextSetLineWidth = quartz.CGContextSetLineWidth

#void CGContextSetRGBFillColor(CGContextRef c, CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha);
CGContextSetRGBFillColor = quartz.CGContextSetRGBFillColor
CGContextSetRGBFillColor.argtypes=[c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]
CGContextSetRGBStrokeColor = quartz.CGContextSetRGBStrokeColor
CGContextSetRGBStrokeColor.argtypes=[c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]

CGDataProviderCreateWithFilename = quartz.CGDataProviderCreateWithFilename
CGImageCreateWithJPEGDataProvider = quartz.CGImageCreateWithJPEGDataProvider
CGImageCreateWithPNGDataProvider = quartz.CGImageCreateWithPNGDataProvider
CGImageDestinationAddImage = quartz.CGImageDestinationAddImage
CGImageDestinationFinalize = quartz.CGImageDestinationFinalize
CGImageGetHeight = quartz.CGImageGetHeight
CGImageGetWidth = quartz.CGImageGetWidth


#void CGPathAddLineToPoint(CGMutablePathRef path, const CGAffineTransform *m, CGFloat x, CGFloat y);
CGPathAddLineToPoint = quartz.CGPathAddLineToPoint
CGPathAddLineToPoint.argtypes=[c_void_p, c_void_p, CGFloat, CGFloat]
CGPathCreateMutable = quartz.CGPathCreateMutable

#void CGPathMoveToPoint(CGMutablePathRef path, const CGAffineTransform *m, CGFloat x, CGFloat y);
CGPathMoveToPoint = quartz.CGPathMoveToPoint
CGPathMoveToPoint.argtypes=[c_void_p, c_void_p, CGFloat, CGFloat]

def CGImageDestinationCreateWithURL(a, b, c, d):
    # arg 2 needs to be nsstring
    return quartz.CGImageDestinationCreateWithURL(a, ns(b), c, d)

